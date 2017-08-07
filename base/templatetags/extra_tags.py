from django import template
from base.models import Sensor, TemperatureSensor, HumiditySensor, ReadValue

register = template.Library()

@register.filter
def getTypeOfSensor(sensorid):
    if (TemperatureSensor.objects.filter(sensorId = sensorid)):
        return "Sensor de temperatura"
    if (HumiditySensor.objects.filter(sensorId = sensorid)):
        return "Sensor d'humitat"

@register.filter
def getShortTypeOfSensor(sensorid):
    if (TemperatureSensor.objects.filter(sensorId = sensorid)):
        return "TEMPERATURA"
    if (HumiditySensor.objects.filter(sensorId = sensorid)):
        return "HUMITAT"

@register.filter
def getLasValueOfSensor(sensorid):
    try:
        valor = ReadValue.objects.filter(sensor__sensorId=sensorid).order_by('-time')[0]

    except Exception as e:
        return 0

    return valor.value
