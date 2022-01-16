from django.contrib import admin
from .models import DeviceType, Manufacturer, Processors, Memories, Harddisks, Graphiccards, Devices
# Register your models here.
admin.site.register(DeviceType)
admin.site.register(Manufacturer)
admin.site.register(Processors)
admin.site.register(Memories)
admin.site.register(Harddisks)
admin.site.register(Graphiccards)
admin.site.register(Devices)