from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# UNIQUE constraint failed user_info.user_id
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, null=True)
    area = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, null=True)
    month = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username
