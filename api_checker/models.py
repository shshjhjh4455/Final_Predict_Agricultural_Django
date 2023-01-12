from django.db import models

class Result(models.Model):
    date = models.DateField()
    tm= models.IntegerField(default=0)
    area = models.IntegerField()
    pred_1 = models.IntegerField()
    pred_2 = models.IntegerField()
    pred_3 = models.IntegerField()
    pred_4 = models.IntegerField()
    pred_5 = models.IntegerField()
    pred_10 = models.IntegerField()
    pred_20 = models.IntegerField()
    pred_60 = models.IntegerField()
    pred_120 = models.IntegerField()
