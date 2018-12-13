from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from .models import Monitor, Result


class MonitorDetailView(View):
    def slug_to_ip_address(self, slug):
        # replace the slug's hyphens with periods
        return slug.replace("-", ".")

    def get_monitor(self, slug, ip_address):
        # make sure the user is accessing the right page for their ip address
        if self.slug_to_ip_address(slug) == ip_address:
            try:
                # get a monitor based on slug if it exists
                monitor = Monitor.objects.get(slug=slug)
            except Monitor.DoesNotExist:
                # create a new monitor if none exists
                monitor = Monitor.objects.create(ip_address=ip_address)

            # update last_viewed for this monitor and save the changes
            monitor.last_viewed = timezone.now()
            monitor.save()

            return monitor

        raise Http404

    def get_results(self, monitor):
        # get the monitor's results
        return Result.objects.filter(monitor=monitor).order_by('-date_created')

    def get(self, request, *args, **kwargs):
        # get the user's ip address
        ip_address = self.request.META['REMOTE_ADDR']

        # store the url slug
        slug = self.kwargs['slug']

        # get this monitor or create a new one
        monitor = self.get_monitor(slug, ip_address)

        # get the monitor's results
        results = self.get_results(monitor)

        return render(request, 'monitors/monitor_detail.html', {
            'ip_address': ip_address,
            'monitor': monitor,
            'results': results,
        })
