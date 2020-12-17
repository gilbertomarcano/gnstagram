from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    """
    Profile model.

    Proxy model that extends the base data with other information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = CloudinaryField('avatar', default="default-profile_dor4jw.png")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return username.
        """
        return self.user.username
