from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class PredictionMade(models.Model):
    avr1 = models.FloatField()
    max1 = models.FloatField()
    min1 = models.FloatField()
    rain1 = models.FloatField()
    sun1 = models.FloatField()
    avr2 = models.FloatField()
    max2 = models.FloatField()
    min2 = models.FloatField()
    rain2 = models.FloatField()
    sun2 = models.FloatField()
    avr3 = models.FloatField()
    max3 = models.FloatField()
    min3 = models.FloatField()
    rain3 = models.FloatField()
    sun3 = models.FloatField()

    def __str__(self):
        return (
            self.avr1
            + self.max1
            + self.min1
            + self.rain1
            + self.sun1
            + self.avr2
            + self.max2
            + self.min2
            + self.rain2
            + self.sun2
            + self.avr3
            + self.max3
            + self.min3
            + self.rain3
            + self.sun3
        )
