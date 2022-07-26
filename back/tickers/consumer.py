import json
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from tickers.models import Ticker
 

@sync_to_async
def get_all_tickers():
    return list(Ticker.objects.all())


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        adict = {}
        while True:
            for ticker in await get_all_tickers():
                await ticker.generate_movement()
                adict[ticker.name] = ticker.value
            await self.send(text_data=json.dumps({'message': adict}))
            await sleep(1)
