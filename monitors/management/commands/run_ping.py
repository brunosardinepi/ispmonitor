import subprocess

from django.core.management.base import BaseCommand, CommandError

from monitors.models import Monitor, Result


class Command(BaseCommand):
    help = "Runs a ping and traceroute to the target host"

    def create_result(self, monitor):
        # setup the ping and traceroute with the monitor's ip address
        processes = [
            ["ping", "-c", "4", monitor.ip_address],
            ["traceroute", monitor.ip_address],
        ]

        # empty variable to hold the ping and traceroute
        content = ""

        for process in processes:
            result = subprocess.Popen(
                args=process,
                bufsize=1,
                universal_newlines=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            # store the output and errors
            output, errors = result.communicate()

            # add to the content variable
            content += "\n{}".format(output)

        # create a result for this monitor
        Result.objects.create(
            monitor=monitor,
            content=content,
        )


    def handle(self, *args, **options):
        # get all of the monitors
        monitors = Monitor.objects.all()

        if monitors:
            for monitor in monitors:
                self.create_result(monitor)
