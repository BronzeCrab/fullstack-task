import json
import time
from channels.generic.websocket import WebsocketConsumer

from tickers.models import Ticker
 

class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:
            alist = []
            for ticker in Ticker.objects.all():
                ticker.generate_movement()
                alist.append({'name': ticker.name, 'value': ticker.value})
            self.send(text_data=json.dumps({'message': alist}))
            time.sleep(1)
