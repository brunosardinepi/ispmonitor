from django.core.management.base import BaseCommand
from django.utils import timezone

from monitors.models import Monitor, Result


class Command(BaseCommand):
    def handle(self, *args, **options):
        # define time range as 7 days
        time_range = timezone.now() - timezone.timedelta(days=7)

        # delete monitors that haven't been viewed in 7 days
        Monitor.objects.filter(last_viewed__lt=time_range).delete()

        # delete results older than 7 days that are saved
        Result.objects.filter(is_saved=True, date_created__lt=time_range).delete()

