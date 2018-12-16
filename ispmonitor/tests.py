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
            '/no-ip/',
            '/sitemap.xml',
            '/robots.txt',
        ]

        for page in pages:
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200)

    def test_home_page_no_ip(self):
        """no client ip is found"""

        # view the home page
        client = Client(REMOTE_ADDR="")
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
