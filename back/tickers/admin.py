from django.contrib import admin

from tickers.models import Ticker, TickerHistory


@admin.register(Ticker)
class TickerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    actions = ['erase_values']


@admin.register(TickerHistory)
class TickerHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticker_id', 'value', 'created_at')
    list_filter = ('ticker_id',)
