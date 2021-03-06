from decimal import Decimal
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

        # strip whitespace off the ends of the content
        content = content.strip()

        # split the ping/traceroute content into lines
        lines = content.splitlines()

        # find the line that has "packet loss"
        packet_loss = [x for x in lines if "packet loss" in x]
        if packet_loss:
            # isolate the packet loss number
            packet_loss = packet_loss[0]
            packet_loss = packet_loss.split(",")[2]
            packet_loss = packet_loss.split("%")[0]
            packet_loss = packet_loss.strip()
            packet_loss = int(packet_loss)
        else:
            # couldn't find "packet loss" in output, so must not be a normal response
            packet_loss = 100

        # find the line that has "min/avg/max/mdev"
        latency = [x for x in lines if "min/avg/max/mdev" in x]
        if latency:
            # isolate the "avg" latency
            latency = latency[0]
            latency = latency.split("/")[4]
            latency = latency.strip()
            latency = Decimal(latency)
        else:
            # couldn't find "latency" in output, so must not be a normal response
            latency = Decimal(9999)

        # create a result for this monitor
        result = Result.objects.create(
                   monitor=monitor,
                   content=content,
                   packet_loss=packet_loss,
                   latency=latency,
               )

        # if latency is >= 300 ms or packet loss is > 0%, save the result
        if latency >= 300 or packet_loss > 0:
            result.is_saved = True
            result.save()

        # return the result
        return result

    def handle(self, *args, **options):
        # get all of the monitors
        monitors = Monitor.objects.all()

        if monitors:
            for monitor in monitors:
                self.create_result(monitor)
