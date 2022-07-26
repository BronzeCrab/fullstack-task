from random import random
from django.db import models
from channels.db import database_sync_to_async


class Ticker(models.Model):
    name = models.CharField(max_length=9)
    value = models.IntegerField()
    
    @database_sync_to_async
    def generate_movement(self):
        movement = -1 if random() < 0.5 else 1
        self.value += movement
        self.save()
