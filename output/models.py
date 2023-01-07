from django.db import models


class PredictionOutput(models.Model):
    area = models.IntegerField(max_length=100)

    def __str__(self):
        return self.area
