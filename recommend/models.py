from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User



class PredictionInput(models.Model):
    location = models.CharField(max_length=20, null=True)
    month = models.DateField(max_length=20, null=True)

    def __str__(self):
        return self.location, self.month
