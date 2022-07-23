from django.test import RequestFactory, TestCase
from tickers.models import Ticker
from tickers.views import index


class TickerTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_ticker_movement(self):
        ticker = Ticker.objects.get(id=1)
        self.assertEqual(ticker.value, 0)
        ticker.generate_movement()
        self.assertNotEqual(ticker.value, 0)

    def test_index_view(self):
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('hello', str(response.content))
