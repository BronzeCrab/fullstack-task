from django.urls import path

from tickers.consumer import Consumer


websocket_urlpatterns = [
    path(r'ws/some_url/', Consumer.as_asgi()),
]
