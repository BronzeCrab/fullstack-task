from django.test import TestCase
from tickers.models import Ticker


class TickerTestCase(TestCase):
    def setUp(self):
        pass

    def test_ticker_movement(self):
        ticker = Ticker.objects.first()
        self.assertEqual(ticker.value, 0)
        ticker.generate_movement()
        ticker = Ticker.objects.get(id=ticker.id)
        self.assertNotEqual(ticker.value, 0)

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('hello', str(response.content))
