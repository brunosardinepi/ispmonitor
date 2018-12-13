from django.http import Http404
from django.utils import timezone

from .models import Monitor, Result


def slug_to_ip_address(slug):
    # replace the slug's hyphens with periods
    return slug.replace("-", ".")

def get_monitor_or_create(slug, ip_address):
    # make sure the user is accessing the right page for their ip address
    if slug_to_ip_address(slug) == ip_address:
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
