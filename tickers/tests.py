from django.test import TestCase
from tickers.models import Ticker


class TickerTestCase(TestCase):
    def setUp(self):
        pass

    def test_ticker_movement(self):
        ticker = Ticker.objects.get(id=1)
        self.assertEqual(ticker.value, 0)
        ticker.generate_movement()
        self.assertNotEqual(ticker.value, 0)
