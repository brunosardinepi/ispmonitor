from django.shortcuts import render
from django.utils import timezone
from django.views import View

from .models import Monitor


class MonitorDetailView(View):
    def get_monitor(self, slug, ip_address):
        try:
            # get a monitor based on slug if it exists
            monitor = Monitor.objects.get(slug=slug)
        except Monitor.DoesNotExist:
            # create a new monitor if none exists
            monitor = Monitor.objects.create(ip_address=ip_address)

        # update last_viewed for this monitor
        monitor.last_viewed = timezone.now()
        monitor.save()

        return monitor

    def get(self, request, *args, **kwargs):
        # get the user's ip address
        ip_address = self.request.META['REMOTE_ADDR']

        # store the url slug
        slug = self.kwargs['slug']

        # get this monitor or create a new one
        monitor = self.get_monitor(slug, ip_address)

        return render(request, 'monitors/monitor_detail.html', {
            'ip_address': ip_address,
            'monitor': monitor,
        })
