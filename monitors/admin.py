from django.contrib import admin

from .models import Monitor, Result


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'date_created', 'last_viewed',)
    ordering = list_display

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('monitor', 'date_created',)
    ordering = list_display
