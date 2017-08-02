from django.conf.urls import url, include

from . import views
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
  url(r'^$', views.index, name='index'),
]

admin.site.site_header = _("Control temperatures")
admin.site.site_title = _("Control temperatures")