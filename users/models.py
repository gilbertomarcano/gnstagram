from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser, UserManager
# class UserManager(BaseUserManager):
#     def create_user(self, username, person, password=None):
#         if not username:
#             raise ValueError('User must have a valid username')

#         user = self.model(username=username, created=datetime.now(), must_change_password=True, deleted=False, person=person)

#         user.set_password(password)
#         user.save(using=self._db)
#         return user


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    picture = CloudinaryField('avatar', default="default-profile_dor4jw.png")
    website = models.CharField(max_length=64, blank=True)
    biography = models.CharField(max_length=64, blank=True)

    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now=True)
    # class Meta(AbstractUser.Meta):
    #     swappable = "AUTH_USER_MODEL"
    

# class Profile(models.Model):
#     """
#     Profile model.

#     Proxy model that extends the base data with other information.
#     """

#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     website = models.URLField(max_length=200, blank=True)
#     biography = models.TextField(blank=True)
#     phone_number = models.CharField(max_length=20, blank=True)
#     picture = CloudinaryField('avatar', default="default-profile_dor4jw.png")

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         """
#         Return username.
#         """
#         return self.user.username
