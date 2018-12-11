from django.http import Http404
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ip_address'] = self.request.META['REMOTE_ADDR']
        return context

def handler404(request):
    raise Http404
