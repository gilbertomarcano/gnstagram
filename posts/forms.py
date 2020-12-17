"""
Post forms.
"""

from django import forms
from cloudinary.uploader import upload
from cloudinary.forms import CloudinaryFileField

from posts.models import Post

class PostForm(forms.ModelForm):
    """
    Post model form.
    """

    photo = CloudinaryFileField(
        options = {
            'folder': 'gnstagram'
        }
    )

    class Meta:
        """
        Form settings.
        """
        model = Post
        fields = {'user', 'profile', 'title', 'photo'}
    
