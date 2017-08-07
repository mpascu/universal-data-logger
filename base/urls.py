from django.conf.urls import url, include

from . import views
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^summary/$', views.summary, name='summary'),
  url(r'^summary/(?P<sensorid>\d+)/$', views.sensor_detail, name='sensor_detail'),
]

admin.site.site_header = _("Universal Data Logger")
admin.site.site_title = _("Universal Data Logger")