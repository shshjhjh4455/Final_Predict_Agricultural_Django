from django.db import models

# Create your models here.


class baechoo_new(models.Model) : 
    year = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=20)
    month= models.IntegerField(blank=True, null=True)
    avr = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    rain = models.FloatField(blank=True, null=True)
    sun = models.FloatField(blank=True, null=True)
