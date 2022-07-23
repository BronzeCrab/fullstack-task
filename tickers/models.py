from random import random
from django.db import models


class Ticker(models.Model):
    name = models.CharField(max_length=9)
    value = models.IntegerField()

    def generate_movement(self):
        movement = -1 if random() < 0.5 else 1
        self.value += movement
