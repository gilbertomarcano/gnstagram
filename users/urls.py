"""
Users URLs.
"""
from django.urls import path
from users import views


from users import views

urlpatterns = [
    # Managment
    path(route='login/', view=views.LoginView.as_view(), name='login'),
    path(route='logout/', view=views.LogoutView.as_view(), name='logout'),
    path(route='edit/profile/', view=views.UpdateProfileView.as_view(), name='update_profile'),
    path(route='edit/account/', view=views.UpdateUserView.as_view(), name='update_account'),
    path(route='signup/', view=views.SignupView.as_view(), name='signup'),

    # Posts
    path(route='<str:username>/', view=views.UserDetailView.as_view(), name='detail'),

    

    
]