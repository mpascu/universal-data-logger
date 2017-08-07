from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Sensor, ReadValue

# Time, timezone related imports
from datetime import datetime as dati, timedelta
import pytz


# @login_required
def index(request):
    return render(request, 'base/index.html')


@login_required
def summary(request):
    sensors = Sensor.objects.filter()
    return render(request, 'base/summary.html', {'sensors': sensors})


@login_required
def sensor_detail(request, sensorid):
    sensor = Sensor.objects.get(sensorId=sensorid)
    values = ReadValue.objects.filter(sensor__sensorId=sensor.sensorId,
                                      time__gt=dati.now(pytz.timezone('Europe/Madrid')) - timedelta(days=1),
                                      time__lt=dati.now(pytz.timezone('Europe/Madrid')))
    sensors = dict()
    sensors[sensor.name] = values

    values_week = ReadValue.objects.filter(sensor__sensorId=sensor.sensorId,
                                           time__gt=dati.now(pytz.timezone('Europe/Madrid')) - timedelta(days=7),
                                           time__lt=dati.now(pytz.timezone('Europe/Madrid')))
    week_values = dict()
    week_values[sensor.name] = values_week

    return render(request, 'base/sensor_detail.html',
                  {'sensors': sensors, 'sensor': sensor, 'week_values': week_values})


def login(request):
    return render(request, auth_views.login)