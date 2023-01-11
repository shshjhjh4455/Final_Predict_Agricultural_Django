from django.db import models


class Predictiprice(models.Model):
    area = models.IntegerField()

    def __str__(self):
        return self.area
