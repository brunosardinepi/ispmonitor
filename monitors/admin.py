from django.contrib import admin

from .models import Monitor


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'date_created', 'last_viewed',)
    ordering = list_display
