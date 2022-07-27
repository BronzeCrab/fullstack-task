from django.test import TestCase


class TickerTestCase(TestCase):
    def setUp(self):
        pass

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('hello', str(response.content))

    def test_ticker_names_view(self):
        response = self.client.get('/ticker_names/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
