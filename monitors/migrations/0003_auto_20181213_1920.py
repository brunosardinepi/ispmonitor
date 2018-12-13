# Generated by Django 2.1.4 on 2018-12-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitors', '0002_result_is_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='last_latency',
            field=models.CharField(default='0 ms', max_length=50),
        ),
        migrations.AddField(
            model_name='monitor',
            name='last_packet_loss',
            field=models.IntegerField(default=0),
        ),
    ]
