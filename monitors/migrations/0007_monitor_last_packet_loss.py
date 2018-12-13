# Generated by Django 2.1.4 on 2018-12-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0006_remove_monitor_last_packet_loss'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='last_packet_loss',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10),
        ),
    ]
