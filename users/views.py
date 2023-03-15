"""
User views.
"""
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.utils import IntegrityError
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import get_user_model

from posts.models import Post
from users import forms, models
from cloudinary.forms import CloudinaryFileField


User = get_user_model()
# Create your views here.
class LoginView(auth_views.LoginView):
    """
    Login view.
    """
    template_name = "users/login.html"

class LogoutView(auth_views.LogoutView):
    """
    Logout view.
    """
    template_name = "users/logged_out.html"

@login_required
def logout_view(request):
    """
    Logout a user.
    """
    logout(request)
    return redirect('users:login')

class SignupView(FormView):
    """
    Users sign up view.
    """
    template_name = 'users/signup.html'
    form_class = forms.SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
        Save form data.
        """
        form.save()
        return super().form_valid(form)

# UserForm is not required with this UpdateView if we use fields attribute
# Using fields attribute means that it depends on model (no validation)
# Using form_class attribute means that it has its own validation
#   It should inheritet from forms.ModelForm
#   It should have a Meta Class
#       It should have model attribute
#       It should have fields attribute with same model fields


class UpdateAccountView(LoginRequiredMixin, UpdateView):
    """
    View for updating an user, with a response rendered by a template.
    """
    template_name = 'users/update/account.html'
    model = User
    form_class = forms.UserForm

    # Defined because generic detail view UpdateUserView must be called with either an object pk or a slug in the URLconf.
    def get_object(self):
        """
        Return user.
        """
        return self.request.user # This is the object to be updated (?)

    def get_success_url(self):
        """
        Return to user.
        """
        username = self.object.username
        update_session_auth_hash(self.request, self.object)  # Important!
        return reverse('users:detail', kwargs={'username': username})
    
    # Add request to form's kwargs using a class-based view
    def get_form_kwargs(self):
        print('update account???')
        kwargs = super(UpdateUserView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class UpdateUserView(LoginRequiredMixin, UpdateView):
    """
    View for updating a profile, with a response rendered by a template.
    """
    template_name = 'users/update/profile.html'
    picture = CloudinaryFileField(
        options = {
            'folder': 'gnstagram'
       }
    )
    model = models.User
    form_class = forms.UserForm

    # Defined because generic detail view UpdateUserView must be called with either an object pk or a slug in the URLconf.
    def get_object(self):
        """
        Return user.
        """
        return self.request.user

    def get_success_url(self):
        """
        Return to user's profile
        """
        print('update user???')
        username = self.object.username
        print(self)
        print(self.object)
        print(self.object.picture)

        return reverse('users:detail', kwargs={'username': username})


class UpdateAccountView(LoginRequiredMixin, UpdateView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    User detail view.
    """
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """
        Add user's post to context.
        """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
