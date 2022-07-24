from django.urls import path

from tickers.consumer import Consumer


websocket_urlpatterns = [
    path(r'ws/', Consumer.as_asgi()),
]
