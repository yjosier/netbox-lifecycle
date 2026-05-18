from dcim.models import Device, DeviceType, Module, ModuleType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from netbox.models import PrimaryModel