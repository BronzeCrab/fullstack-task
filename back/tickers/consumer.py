import json
import time
from channels.generic.websocket import WebsocketConsumer

from tickers.models import Ticker
 

class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        adict = {}
        while True:
            for ticker in Ticker.objects.all():
                ticker.generate_movement()
                adict[ticker.name] = ticker.value
            self.send(text_data=json.dumps({'message': adict}))
            time.sleep(1)
