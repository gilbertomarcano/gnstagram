# Django modules
from django import forms

# Apps modules
from comments.models import Comment

# Cloudinary modules
from cloudinary.forms import CloudinaryFileField

class CommentForm(forms.ModelForm):
    """
    Comment model form.
    """
    class Meta:
        """
        Form settings.
        """
        model = Comment
        fields = ('user', 'posts', 'text')  # Change to dict if works

    