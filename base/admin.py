from django.contrib import admin
from .models import ReadValue
from .models import AveragedValue
from .models import Sensor
from .models import TemperatureSensor
from .models import HumiditySensor
from .models import Receiver
from .models import Alarm
from .models import DataloggerDevice
from .models import ConnectionLostAlarm
from .models import TemperatureAlarm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(ReadValue)
admin.site.register(AveragedValue)
admin.site.register(Sensor)
admin.site.register(TemperatureSensor)
admin.site.register(HumiditySensor)
admin.site.register(Receiver)
#admin.site.register(Alarm)
admin.site.register(DataloggerDevice)
admin.site.register(ConnectionLostAlarm)
admin.site.register(TemperatureAlarm)
