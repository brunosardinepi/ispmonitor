from django.contrib import admin
from django.urls import path

from . import config
from . import views
from monitors.views import MonitorDetailView


urlpatterns = [
    path('{}/'.format(config.settings['admin']), admin.site.urls),
    path('<slug:slug>/', MonitorDetailView.as_view(), name='monitor_detail'),
    path('', views.HomeView.as_view(), name='home'),
]
