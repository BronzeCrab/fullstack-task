from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse

from tickers.models import Ticker


class IndexView(TemplateView):
    template_name = 'index.html'


class TickerNamesView(View):
    def get(self, request):
        ticker_names_list = Ticker.objects.values_list('name', flat=True)
        return JsonResponse([x for x in ticker_names_list], safe=False)
