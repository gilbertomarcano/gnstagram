"""
Users URLs.
"""
from django.urls import path
from comments import views

urlpatterns = [
    # Managment
    path(route='create', view=views.CreateCommentView.as_view(), name='create_comment'),
]

