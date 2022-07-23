from django.contrib import admin

from tickers.models import Ticker


@admin.register(Ticker)
class TickerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
    actions = ['erase_values']

    @admin.action(description='Erase all values of all tickers')
    def erase_values(modeladmin, request, queryset):
        queryset.update(value=0)
