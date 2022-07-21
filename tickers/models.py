from django.db import models


class Ticker(models.Model):
    name = models.CharField(max_length=9)
    value = models.IntegerField()
