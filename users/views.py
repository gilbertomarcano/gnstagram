"""
User views.
"""
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.db.utils import IntegrityError
from django.views.generic import DetailView, FormView, UpdateView

from posts.models import Post
from users.models import Profile
from users.forms import ProfileForm, SignupForm


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
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
        Save form data.
        """
        form.save()
        return super().form_valid(form)


############################
#   OLD SIGNUP V2.0        #
############################
# def signup(request):
#     """
#     Signup view.
#     """
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()

#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form': form}
#     )
    

    ############################
    #   OLD SIGNUP             #
    ############################
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     password_confirmation = request.POST['password_confirmation']

    #     if password != password_confirmation:
    #         return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
    #     try:
    #         user = User.objects.create_user(username=username, password=password)
    #     except IntegrityError:
    #         return render(request, 'users/signup.html', {'error': 'Username is already used'})
        
    #     user.first_name = request.POST['first_name']
    #     user.last_name = request.POST['last_name']
    #     user.email = request.POST['email']
    #     user.save()

    #     profile = Profile(user=user)
    #     profile.save()

    #     return redirect('login')


    # return render(request, 'users/signup.html')

# ProfileForm is not required with this UpdateView if we use fields attribute
# Using fields attribute means that it depends on model (no validation)
# Using form_class attribute means that it has its own validation
#   It should inheritet from forms.ModelForm
#   It should have a Meta Class
#       It should have model attribute
#       It should have fields attribute with same model fields
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """
    Update profile view.
    """

    template_name = 'users/update.html'
    model = Profile
    # fields = ['website', 'biography', 'phone_number', 'picture'] # ProfileForm
    form_class = ProfileForm

    def get_object(self):
        """
        Return user's profile.
        """
        return self.request.user.profile

    def get_success_url(self):
        """
        Return to user's profile
        """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

    # def form_valid(self, form):
    #     """
    #     Save form data.
    #     """
    #     print(form)
    #     input('...')
    #     form.save()
    #     return super().form_valid(form)

    # def form_valid(self, form):
    #     data = self.get_form_kwargs()['data']
    #     print('\n\n\n\n===========IM IN FORM================')
    #     print(data)

    #     print('\n================================================\n')
    #     print(data['biography'])
        

    #     print('\n================================================\n')
    #     return super().form_valid(form)
        
    # def get_context_data(self, **kwargs):
    #     """
    #     Add (?) data to context.
    #     """
    #     context = super().get_context_data(**kwargs)
    #     print(context)
        
    #     return context

# ###########################
#   OLD UPDATE              #
#############################
# @login_required
# def update_profile(request):
#     """
#     Update a user's profile view.
#     """
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data

#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()

#             url = reverse('users:detail', kwargs={'username':request.user.username})
#             return redirect(url)
#     else:
#         form = ProfileForm()

#     return render(
#         request=request,
#         template_name='users/update.html',
#         context={
#             'profile': profile,
#             'user': request.user,
#             'form': form
#         }
#     )




class UserDetailView(LoginRequiredMixin, DetailView):
    """
    User detail view.
    """
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    # def get(self, request, *args, **kwargs):
    #     """
    #     Handle errors.
    #     """
        
    #     try:
    #         self.object = self.get_object()
    #         print('\n\nget get get\n\n')
    #         print(request.user)
    #         print('\n\nget get get\n\n')
    #         # return reverse('users:detail', kwargs={'username': request.user})
    #         return super().get(request, *args, **kwargs)
    #     except:
    #         # This handle 404 error for exaple
    #         print('Value error value error')
    #         return redirect('posts:feed')
    
    def get_context_data(self, **kwargs):
        """
        Add user's post to context.
        """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
