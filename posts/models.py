""" Post models. """
# Django modules
from django.db import models

# Cloudinary modules
from cloudinary.models import CloudinaryField

from users.models import User

# Create your models here.
class Post(models.Model):
    """
    Post model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = CloudinaryField('image')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return title and username.
        """
        return '{} by @{}'.format(self.title, self.user.username)