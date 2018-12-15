from django.test import Client, TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_pages(self):
        pages = [
            '/',
            '/donate/',
            '/help/',
            '/privacy-policy/',
        ]

        for page in pages:
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200)
