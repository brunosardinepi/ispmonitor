from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path

from . import config
from . import views
from monitors.views import MonitorDetailView, ResultDetailView


urlpatterns = [
    path('{}/'.format(config.settings['admin']), admin.site.urls),
    path('result/<int:pk>/', ResultDetailView.as_view(), name='result_detail'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('donate/', views.DonateView.as_view(), name='donate'),
    path('privacy-policy/', views.PrivacyView.as_view(), name='privacy'),
    path('no-ip/', views.NoIPView.as_view(), name='no-ip'),
    path('<slug:slug>/', MonitorDetailView.as_view(), name='monitor_detail'),
    path('', views.HomeView.as_view(), name='home'),

    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),
]
