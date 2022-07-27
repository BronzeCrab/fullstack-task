from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse

from tickers.models import Ticker


class IndexView(TemplateView):
    """Ендпоинт для мониторинга работы бэка."""
    template_name = 'index.html'


class TickerNamesView(View):
    """Ендпоинт для заполнения селекта на фронте."""
    def get(self, request):
        ticker_names_list = Ticker.objects.values_list('name', flat=True)
        return JsonResponse([x for x in ticker_names_list], safe=False)
