from django.contrib import admin

from tickers.models import Ticker


@admin.register(Ticker)
class TickerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
