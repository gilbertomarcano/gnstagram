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

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        # if 'title' in cleaned_data and 'photo' in cleaned_data:
        #     print('UPLOADED CORRECTLY\n----------\n')
        #     cloudinary.uploader.upload(cleaned_data['photo'])
   

    class Meta:
        """
        Form settings.
        """
        model = Post
        fields = {'user', 'profile', 'title', 'photo'}