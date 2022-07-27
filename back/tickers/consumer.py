import json
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from tickers.models import Ticker
 

@sync_to_async
def get_all_tickers():
    return list(Ticker.objects.all())


@sync_to_async
def get_history_for_ticker(ticker, ind):
    try:
        hist = list(ticker.tickerhistory_set.order_by('created_at').all())[ind]
    except Exception:
        return None
    return hist


@sync_to_async
def get_last_history_for_ticker(ticker):
    return ticker.tickerhistory_set.order_by('created_at').last()


class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        ind = 0
        while True:
            adict = {}
            for ticker in await get_all_tickers():
                adict[ticker.name] = []
                history = await get_history_for_ticker(ticker, ind)
                if not history:
                    await ticker.generate_movement()
                    history = await get_last_history_for_ticker(ticker)
                adict[ticker.name] = [
                    history.value,
                    history.created_at.strftime('%H:%M:%S:%f')[:-5],
                ]
            ind += 1
            await self.send(text_data=json.dumps({'message': adict}))
            await sleep(1)
