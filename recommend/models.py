from django.db import models


class PredictionInput(models.Model):
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
    result = models.IntegerField()

    def __str__(self):
        return self.result
        

