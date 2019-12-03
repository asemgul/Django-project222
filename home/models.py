from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Day(models.Model):
  day_of_month = models.IntegerField()

  def __str__(self):
    return str(self.day_of_month)


class City(models.Model):
  city_name = models.CharField(max_length=100)

  def __str__(self):
    return self.city_name;


class Airport(models.Model):
  airport_name = models.CharField(max_length=100)
  airport_city = models.ForeignKey(City, on_delete=models.CASCADE)

  def __str__(self):
    return self.airport_name


class Flight(models.Model):
  from_city = models.ForeignKey(City, on_delete=models.CASCADE)
  to_city = models.ForeignKey(City, related_name="to_city", on_delete=models.CASCADE)
  fligth_start_time = models.TimeField(default="00:00")
  flight_end_time = models.TimeField(default="00:00")
  flight_duration = models.IntegerField()
  flight_price_econom = models.FloatField()
  flight_price_business = models.FloatField()
  flight_days = models.ManyToManyField(Day)
  fligth_econom_places = models.IntegerField(default=60)
  flight_business_places = models.IntegerField(default=10)


class User(AbstractUser):
    patronymic_name = models.CharField(max_length=55)
    telephone = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username


class Flightofusers(models.Model):
    from_c = models.CharField(max_length=180)
    to_c = models.CharField(max_length=180)
    date=models.DateTimeField(auto_now_add=True)
    cost=models.CharField(max_length=180)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.from_c

    def get_absolute_url(self):
        return reverse('flight-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)