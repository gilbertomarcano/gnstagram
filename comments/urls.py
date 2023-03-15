"""
Users URLs.
"""
from django.urls import path
from comments import views

urlpatterns = [
    # Managment
    path(route='create', view=views.create, name='create_comment'),
    path(route='<slug:pk>', view=views.CommentDetailView.as_view(), name='detail_view')
]

