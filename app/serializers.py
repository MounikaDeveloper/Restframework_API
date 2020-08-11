import pytz
from rest_framework import serializers

from django.db import models

from app.models import UserModel1


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    password = serializers.CharField()
    real_name = serializers.CharField()
    tz = serializers.CharField()


class ActivitySerializer(serializers.Serializer):
    # activity = models.ForeignKey(UserModel1,on_delete='CASCADE')
    activity=serializers.CharField()
    start_time = serializers.CharField(max_length=30)
    end_time = serializers.CharField(max_length=30)



