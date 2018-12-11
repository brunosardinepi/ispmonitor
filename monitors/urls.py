from django.urls import path

from . import views


app_name = 'monitors'

urlpatterns = [
#    path('delete/<str:name>/', views.AliasDelete.as_view(), name='alias_delete'),
    path('<slug:slug>/', views.MonitorDetail.as_view(), name='monitor_detail'),
]
