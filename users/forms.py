"""
User forms.
"""
from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from users.models import User

# Profile Form is not longer required since we're using UpdateProfileView
class UserForm(forms.ModelForm):

    current_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(UserForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data['current_password'] if 'current_password' in cleaned_data else 'error'
        new_password = cleaned_data['new_password'] if 'new_password' in cleaned_data else ''
        password_confirmation = cleaned_data['password_confirmation'] if 'password_confirmation' in cleaned_data else ''

        if new_password and new_password == password_confirmation and not current_password:
            raise forms.ValidationError('Current password is missing')
        elif current_password and new_password and new_password == password_confirmation:
            user = self.request.user
            user.set_password(new_password)
            user.save()
    
    def clean_username(self):
        """
        Username must be unique.
        """
        username = self.cleaned_data['username']

        if username != self.request.user.username:
            username_taken = User.objects.filter(username=username).exists()
            if username_taken:
                raise forms.ValidationError('Username is already in use.')
        return username
            
    def clean_current_password(self):
        """
        Validates the current password form.
        """
        current_password = self.cleaned_data['current_password']
        if current_password and not check_password(current_password, self.request.user.password):
            raise forms.ValidationError('Current password is incorrect')
        return current_password
    
    def clean_new_password(self):
        """
        Validates if the new password is valid.
        """
        new_password = self.cleaned_data['new_password']
        if new_password:
            validate_password(new_password)
        return new_password
    
    def clean_password_confirmation(self):
        """
        Validates if the password confirmation matches.
        """
        password_confirmation = self.cleaned_data['password_confirmation']
        print(password_confirmation)
        new_password = self.cleaned_data['new_password'] if 'new_password' in self.cleaned_data else ''
        if new_password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return password_confirmation

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }

class UserForm(forms.ModelForm):
    """
    User form.
    """
    
    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=False)
    # picture = forms.ImageField()

    class Meta:
        model = User
        fields = ['website', 'biography', 'phone_number']
        

class SignupForm(forms.Form):
    """
    Signup form.
    """

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(min_length=8, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())

    def clean_username(self):
        """
        Username must be unique.
        """
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean_email(self):
        """
        Email must be unique.
        """
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()

        if email_taken:
            raise forms.ValidationError('Email is already in use.')
        return email

    def clean(self):
        """
        Verify password confirmation match.
        """
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data
    
    def save(self):
        """
        Create user and profile.
        """
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)