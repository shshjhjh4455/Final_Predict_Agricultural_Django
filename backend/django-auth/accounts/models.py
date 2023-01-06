from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    nickname= models.CharField(default='', max_length=15, null=False, blank=False, unique=True)
    name= models.CharField(default='', max_length=40, null=False, blank=False)

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email', 'name']

    objects = UserManager()

    def __str__(self):
        return self.email
