from django.db import models

# Create your models here.


class inform_baechoo(models.Model) : 
    location = models.CharField(max_length=20)
    season = models.CharField(max_length=10)
    year = models.IntegerField(blank=True, null=True)

    avr_1 = models.FloatField(blank=True, null=True)
    max_1 = models.FloatField(blank=True, null=True)
    min_1 = models.FloatField(blank=True, null=True)
    rain_1 = models.FloatField(blank=True, null=True)
    sun_1 = models.FloatField(blank=True, null=True)

    avr_2 = models.FloatField(blank=True, null=True)
    max_2 = models.FloatField(blank=True, null=True)
    min_2 = models.FloatField(blank=True, null=True)
    rain_2 = models.FloatField(blank=True, null=True)
    sun_2 = models.FloatField(blank=True, null=True)

    avr_3 = models.FloatField(blank=True, null=True)
    max_3 = models.FloatField(blank=True, null=True)
    min_3 = models.FloatField(blank=True, null=True)
    rain_3 = models.FloatField(blank=True, null=True)
    sun_3 = models.FloatField(blank=True, null=True)

    avr_4 = models.FloatField(blank=True, null=True)
    max_4 = models.FloatField(blank=True, null=True)
    min_4 = models.FloatField(blank=True, null=True)
    rain_4 = models.FloatField(blank=True, null=True)
    sun_4 = models.FloatField(blank=True, null=True)

    avr_5 = models.FloatField(blank=True, null=True)
    max_5 = models.FloatField(blank=True, null=True)
    min_5 = models.FloatField(blank=True, null=True)
    rain_5 = models.FloatField(blank=True, null=True)
    sun_5 = models.FloatField(blank=True, null=True)

    avr_6 = models.FloatField(blank=True, null=True)
    max_6 = models.FloatField(blank=True, null=True)
    min_6 = models.FloatField(blank=True, null=True)
    rain_6 = models.FloatField(blank=True, null=True)
    sun_6 = models.FloatField(blank=True, null=True)

    avr_7 = models.FloatField(blank=True, null=True)
    max_7 = models.FloatField(blank=True, null=True)
    min_7 = models.FloatField(blank=True, null=True)
    rain_7 = models.FloatField(blank=True, null=True)
    sun_7 = models.FloatField(blank=True, null=True)

    avr_8 = models.FloatField(blank=True, null=True)
    max_8 = models.FloatField(blank=True, null=True)
    min_8 = models.FloatField(blank=True, null=True)
    rain_8 = models.FloatField(blank=True, null=True)
    sun_8 = models.FloatField(blank=True, null=True)

    avr_9 = models.FloatField(blank=True, null=True)
    max_9 = models.FloatField(blank=True, null=True)
    min_9 = models.FloatField(blank=True, null=True)
    rain_9 = models.FloatField(blank=True, null=True)
    sun_9 = models.FloatField(blank=True, null=True)

    avr_10 = models.FloatField(blank=True, null=True)
    max_10 = models.FloatField(blank=True, null=True)
    min_10 = models.FloatField(blank=True, null=True)
    rain_10 = models.FloatField(blank=True, null=True)
    sun_10 = models.FloatField(blank=True, null=True)

    avr_11 = models.FloatField(blank=True, null=True)
    max_11 = models.FloatField(blank=True, null=True)
    min_11 = models.FloatField(blank=True, null=True)
    rain_11 = models.FloatField(blank=True, null=True)
    sun_11 = models.FloatField(blank=True, null=True)

    avr_12 = models.FloatField(blank=True, null=True)
    max_12 = models.FloatField(blank=True, null=True)
    min_12 = models.FloatField(blank=True, null=True)
    rain_12 = models.FloatField(blank=True, null=True)
    sun_12 = models.FloatField(blank=True, null=True)

    area = models.IntegerField(blank=True, null=True)
    output = models.FloatField(blank=True, null=True)

