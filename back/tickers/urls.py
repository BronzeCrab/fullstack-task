from django.urls import path
from tickers.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
