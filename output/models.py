from django.db import models

# Create your models here.
class PredictionOutput(models.Model):
    area = models.IntegerField(null=True)
    output = models.IntegerField(null=True)
