from django.db import models


class PredictionInput(models.Model):
    location = models.CharField(max_length=20, null=True)
    month = models.IntegerField(null=True)

    def __str__(self):
        return self.location, self.month
