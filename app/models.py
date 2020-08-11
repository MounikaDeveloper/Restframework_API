import pytz
from django.db import models


class UserModel1(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=30)
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')


class ActivityModel1(models.Model):
    activity = models.ForeignKey(UserModel1, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=30)
    end_time = models.CharField(max_length=30)



