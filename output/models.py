from django.db import models

# Create your models here.
class PredictionOutput(models.Model):
    area = models.IntegerField(null=True)

    def __str__(self):
        return self.area