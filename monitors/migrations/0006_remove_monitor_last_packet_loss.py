# Generated by Django 2.1.4 on 2018-12-13 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0005_monitor_last_latency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='last_packet_loss',
        ),
    ]