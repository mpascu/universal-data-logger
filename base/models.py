
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.core.validators import RegexValidator


class DataloggerDevice(models.Model):

    name = models.CharField(max_length=60)
    location = models.CharField(max_length=50)
    alarm_delay = models.IntegerField(default=50)

    def __str__(self):
        return "Registrador de %s, %s" % (self.name, self.location)


class Sensor(models.Model):

    sensorId = models.IntegerField(unique=True, default=0)
    name = models.CharField(max_length=60)
    min_value = models.DecimalField(max_digits=5, decimal_places=2)
    max_value = models.DecimalField(max_digits=5, decimal_places=2)
    alarm_delay = models.IntegerField(default=30)
    datalogger = models.ForeignKey(DataloggerDevice, on_delete=models.PROTECT)

    def __str__(self):
        return "Sensor %d , %s" % (self.sensorId, self.name)


class TemperatureSensor (Sensor):

    def __str__(self):
        return "Sensor de temperatura %d , %s" % (self.sensorId, self.name)


class HumiditySensor (Sensor):

    def __str__(self):
        return "Sensor d'humitat %d , %s" % (self.sensorId, self.name)


class Alarm(models.Model):

    active = models.BooleanField(default=False)
    time_start = models.DateTimeField(editable=True, default=timezone.now)
    time_end = models.DateTimeField(editable=True,
                                    default=None,
                                    null=True,
                                    blank=True)
    description = models.CharField(max_length=300, null=True)

    def __str__(self):
        return "'Origin:' %s - %s - %s" % (
            self.time_start, self.time_end, self.temp_on_activation)


class TemperatureAlarm(Alarm):

    temp_on_activation = models.DecimalField(max_digits=5, decimal_places=2)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "'Origin:'%s - %s - %s - %s" % (
            self.sensor, self.time_start, self.time_end, self.temp_on_activation)


class ConnectionLostAlarm(Alarm):

    datalogger = models.ForeignKey(DataloggerDevice, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "'Origin:'%s - %s - %s - %s" % (
            self.sensor, self.time_start, self.time_end, self.temp_on_activation)


class ReadValue(models.Model):

    value = models.DecimalField(max_digits=5, decimal_places=2)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(editable=False, default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.time = timezone.now().replace(second=0, microsecond=0)
        return super(ReadValue, self).save(*args, **kwargs)

    def __str__(self):
        return "%s , %f  , %s" % (self.sensor, self.value, self.time)


class AveragedValue(models.Model):

    value = models.DecimalField(max_digits=5, decimal_places=2)
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, null=True)
    time = models.DateTimeField(editable=False, default=timezone.now().replace(second=0, microsecond=0))

    def __str__(self):
        return "%s , %f , %s" % (self.sensor, self.value, self.time)


class Receiver(models.Model):

    name = models.CharField(max_length=30)
    sms_active = models.BooleanField(default=0)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be in this format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email_active = models.BooleanField(default=0)
    email = models.EmailField(unique=False, blank=True)
    SMS_life_signal_active = models.BooleanField(default=0)

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.phone_number, self.email)

