from django.db import models

class Result(models.Model):
    date = models.CharField(max_length=20)
    pred_5 = models.FloatField()
    pred_10 = models.FloatField()
    pred_20 = models.FloatField()
    pred_60 = models.FloatField()
    pred_120 = models.FloatField()