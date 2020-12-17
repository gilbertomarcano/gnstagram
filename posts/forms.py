"""
Post forms.
"""
# Django modules
from django import forms

# Apps modules
from posts.models import Post

# Cloudinary modules
from cloudinary.forms import CloudinaryFileField

class PostForm(forms.ModelForm):
    """
    Post model form.
    """
    photo = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'folder': 'gnstagram'
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        print('===============')
        print('===============')
        print('===============')
        print('===============')
        print(cleaned_data)
        print('===============')
        print('===============')
        print('===============')
        print('===============')


    class Meta:
        """
        Form settings.
        """
        model = Post
        fields = ('user', 'profile', 'title', 'photo') # Change to dict if works

    
