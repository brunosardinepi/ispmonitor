from django.test import Client, TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
