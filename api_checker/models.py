from django.db import models


class Result(models.Model):
    date = models.DateField()
    tm = models.IntegerField(default=0)
    item_5 = models.TextField()
    item_20 = models.TextField()
    item_365 = models.TextField()
    area = models.IntegerField(default=0)
    pred_1 = models.IntegerField()
    pred_2 = models.IntegerField()
    pred_3 = models.IntegerField()
    pred_4 = models.IntegerField()
    pred_5 = models.IntegerField()
    pred_10 = models.IntegerField()
    pred_20 = models.IntegerField()
    pred_60 = models.IntegerField()
    pred_120 = models.IntegerField()
