from random import random
from django.db import models
from channels.db import database_sync_to_async


class Ticker(models.Model):
    name = models.CharField(max_length=9)

    @database_sync_to_async
    def generate_movement(self):
        movement = -1 if random() < 0.5 else 1
        last_history = self.tickerhistory_set.order_by('created_at').last()
        self.tickerhistory_set.create(value=last_history.value + movement)

    def __str__(self):
        return self.name


class TickerHistory(models.Model):
    value = models.IntegerField()
    created_at = models.TimeField(auto_now_add=True)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
