from django.db import migrations, models
from django.template.backends import django

from website import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_duration', models.TimeField()),
                ('flight_price_econom', models.FloatField()),
                ('flight_price_business', models.FloatField()),
                ('from_city', models.ManyToManyField(to='home.City')),
                ('to_city', models.ManyToManyField(related_name='to_city', to='home.City')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=100)),
                ('airport_city', models.ManyToManyField(to='home.City')),
            ],
        ),
    ]
