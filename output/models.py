from django.db import models


class PredictionOutput(models.Model):
    area = models.IntegerField()

    def __str__(self):
        return self.area