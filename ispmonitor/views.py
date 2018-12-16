from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from monitors.utils import get_user_ip


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ip_address'] = get_user_ip(self.request)
        return context

class HelpView(TemplateView):
    template_name = 'help.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ip_address'] = get_user_ip(self.request)
        return context

class DonateView(TemplateView):
    template_name = 'donate.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ip_address'] = get_user_ip(self.request)
        return context

class PrivacyView(TemplateView):
    template_name = 'privacy.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ip_address'] = get_user_ip(self.request)
        return context

class NoIPView(TemplateView):
    template_name = 'no_ip.html'

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
