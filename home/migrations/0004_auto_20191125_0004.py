# Generated by Django 2.2.6 on 2019-11-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191124_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='flight_start_time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='flight',
            name='fligth_start_time',
            field=models.TimeField(default='00:00'),
        ),
    ]
