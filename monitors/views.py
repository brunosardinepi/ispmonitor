from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import View

from .models import Monitor, Result
from .utils import get_monitor_or_create, slug_to_ip_address


class MonitorDetailView(View):
    def get(self, request, *args, **kwargs):
        # get the user's ip address
        ip_address = self.request.META['REMOTE_ADDR']

        # store the url slug
        slug = self.kwargs['slug']

        # get this monitor or create a new one
        monitor = get_monitor_or_create(slug, ip_address)

        # get the monitor's saved results
        saved_results = Result.objects.filter(
            monitor=monitor, is_saved=True).order_by('-date_created')

        # get the monitor's saved results
        full_results = Result.objects.filter(
            monitor=monitor).order_by('-date_created')

        # get the monitor's most recent 5 results
        recent_results = full_results[:5]

        # if there are results, get the last result
        last_result = None
        if full_results:
            last_result = full_results[0]

        return render(request, 'monitors/monitor_detail.html', {
            'ip_address': ip_address,
            'monitor': monitor,
            'saved_results': saved_results,
            'full_results': full_results,
            'recent_results': recent_results,
            'last_result': last_result,
        })

class ResultDetailView(View):
    def get(self, request, *args, **kwargs):
        # get the user's ip address
        ip_address = self.request.META['REMOTE_ADDR']

        # get the requested result
        result = get_object_or_404(Result, pk=self.kwargs['pk'])

        # make sure the user has access to this result
        # based on their ip matching the result's monitor's ip
        url_monitor_ip_address = slug_to_ip_address(self.kwargs['slug'])
        if ip_address == url_monitor_ip_address and ip_address == result.monitor.ip_address:
            return render(request, 'monitors/result_detail.html', {
                'ip_address': ip_address,
                'result': result,
            })

        raise Http404
