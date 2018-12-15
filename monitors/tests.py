from django.test import Client, TestCase
from django.utils import timezone

from model_mommy import mommy

from .models import Monitor, Result


class MonitorsTest(TestCase):
    def setUp(self):
        self.client = Client()

        # create monitors for testing
        self.monitors = mommy.make(
            Monitor,
            ip_address='1.1.1.1',
            slug='1-1-1-1',
            _quantity=2,
        )

        # set the 2nd monitor's ip address, then save the changes
        self.monitors[1].ip_address = '2.2.2.2'
        self.monitors[1].slug = '2-2-2-2'
        self.monitors[1].save()

        # create results for testing
        self.results = mommy.make(
            Result,
            monitor=self.monitors[0],
            date_created=timezone.now(),
            _quantity=3,
            _fill_optional=True,
        )

        # set the 2nd result's monitor to the 2nd monitor
        self.results[1].monitor = self.monitors[1]
        self.results[1].save()

        # set the 3rd result's date to 1 day prior to 1st result's date
        self.results[2].date_created = timezone.now() - timezone.timedelta(days=1)
        self.results[2].save()

    def test_monitor_exists(self):
        """ all of the monitors are being created correctly """

        # get all of the monitors
        monitors = Monitor.objects.all()

        # check that each monitor is in our queryset
        for monitor in self.monitors:
            self.assertIn(monitor, monitors)

    def test_result_exists(self):
        """ all of the results are being created correctly """

        # get all of the results
        results = Result.objects.all()

        # check that each result is in our queryset
        for result in self.results:
            self.assertIn(result, results)

    def test_monitor_create(self):
        """if a monitor doesn't exist when going to the monitor_detail view,
        a new monitor should be created for that ip address"""

        # check how many monitors exist right now
        monitors = Monitor.objects.all()
        self.assertEqual(monitors.count(), len(self.monitors))

        # view the monitor_detail page with a new ip address
        ip_address = '3.3.3.3'
        client = Client(REMOTE_ADDR=ip_address)
        slug = ip_address.replace(".", "-")
        response = client.get('/{}/'.format(slug))
        self.assertEqual(response.status_code, 200)

        # check that a new monitor was created
        monitors = Monitor.objects.all()
        monitor = Monitor.objects.get(slug=slug)
        self.assertIn(monitor, monitors)

    def test_monitor_page(self):
        """if a monitor exists when going to the monitor_detail view,
        we should be sent to that monitor page"""

        # view the monitor_detail page
        client = Client(REMOTE_ADDR=self.monitors[0].ip_address)
        response = client.get('/{}/'.format(self.monitors[0].slug))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.monitors[0].ip_address)
        self.assertContains(response, self.results[0].content)
        self.assertNotContains(response, self.results[2].content)

        # viewing a monitor_detail page different than our ip address
        # should result in 404
        response = client.get('/{}/'.format(self.monitors[1].slug))
        self.assertEqual(response.status_code, 404)

    def test_result_page(self):
        """the result_detail page shows the correct result content"""

        # view the result_detail page
        client = Client(REMOTE_ADDR=self.monitors[0].ip_address)
        response = client.get('/result/{}/'.format(self.results[0].pk))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.results[0].content)
