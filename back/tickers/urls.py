from django.urls import path
from tickers.views import IndexView, TickerNamesView

urlpatterns = [
    path('', IndexView.as_view()),
    path('ticker_names/', TickerNamesView.as_view()),
]
