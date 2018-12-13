from django.core.management.base import BaseCommand
from django.utils import timezone

from monitors.models import Result


class Command(BaseCommand):
    help = "Deletes results that are older than 24 hours if not saved"

    def handle(self, *args, **options):
        # define time range as 24 hours
        time_range = timezone.now() - timezone.timedelta(hours=24)

        # delete results older than 24 hours
        Result.objects.filter(date_created__lt=time_range).delete()
