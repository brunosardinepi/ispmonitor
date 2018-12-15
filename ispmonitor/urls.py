from django.contrib import admin
from django.urls import path

from . import config
from . import views
from monitors.views import MonitorDetailView, ResultDetailView


urlpatterns = [
    path('{}/'.format(config.settings['admin']), admin.site.urls),
    path('<slug:slug>/', MonitorDetailView.as_view(), name='monitor_detail'),
    path('result/<int:pk>/', ResultDetailView.as_view(), name='result_detail'),
    path('', views.HomeView.as_view(), name='home'),
]
