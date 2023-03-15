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
    website = models.CharField(max_length=64, blank=True)
    biography = models.CharField(max_length=64, blank=True)

    # class Meta(AbstractUser.Meta):
    #     swappable = "AUTH_USER_MODEL"
    
# print(User.objects)
# from django.contrib.auth import get_user_model
# User = get_user_model()
# print(User.objects)

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     is_active = models.BooleanField(_('active'), default=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#     website = models.CharField(max_length=64, blank=True)
#     biography = models.CharField(max_length=64, blank=True)

#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         unique=True,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#     )

#     is_staff = models.BooleanField(
#         _("staff status"),
#         default=False,
#         help_text=_("Designates whether the user can log into this admin site."),
#     )
#     is_active = models.BooleanField(
#         _("active"),
#         default=True,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )
    
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Sends an email to this User.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)


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
