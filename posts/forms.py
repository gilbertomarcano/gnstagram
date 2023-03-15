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
            'folder': 'gnstagram/posts'
        }
    )

    class Meta:
        """
        Form settings.
        """
        model = Post
        fields = ('title', 'photo') # Change to dict if works

    
