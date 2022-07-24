from django.test import RequestFactory, TestCase
from tickers.models import Ticker
from tickers.views import IndexView


class TickerTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_ticker_movement(self):
        ticker = Ticker.objects.first()
        self.assertEqual(ticker.value, 0)
        ticker.generate_movement()
        ticker = Ticker.objects.get(id=ticker.id)
        self.assertNotEqual(ticker.value, 0)

    def test_index_view(self):
        request = self.factory.get('/')
        response = IndexView.as_view()(request)
        self.assertEqual(response.render().status_code, 200)
        self.assertIn('hello', str(response.content))
