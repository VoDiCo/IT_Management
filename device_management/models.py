from django.db import models
from users.models import User


# Create your models here.
class DeviceType(models.Model):
    device_type_id = models.BigAutoField(primary_key=True)
    device_type_name = models.CharField(max_length=255)
    device_type_shortcut = models.CharField(max_length=4)

    def __str__(self):
        return self.device_type_name


class Manufacturer(models.Model):
    manufacturer_id = models.BigAutoField(primary_key=True)
    manufacturer_name = models.CharField(max_length=255)
    manufacturer_shortcut = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.manufacturer_name} ({self.manufacturer_shortcut})'


class Processors(models.Model):
    processor_id = models.AutoField(primary_key=True)
    processor_name = models.CharField(max_length=30)
    processor_cores = models.IntegerField()
    processor_speed = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Processors'

    def __str__(self):
        return f'{self.processor_name}'


class Memories(models.Model):
    memory_id = models.AutoField(primary_key=True)
    memory_type = models.CharField(max_length=20)
    memory_capacity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Memories'

    def __str__(self):
        return f'{self.memory_capacity} {self.memory_type}'


class Harddisks(models.Model):
    harddisk_id = models.AutoField(primary_key=True)
    harddisk_type = models.CharField(max_length=10)
    harddisk_capacity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Harddisks'

    def __str__(self):
        return f'{self.harddisk_capacity} {self.harddisk_type}'


class Graphiccards(models.Model):
    graphiccard_id = models.AutoField(primary_key=True)
    graphiccard_type = models.CharField(max_length=30)
    graphiccard_capacity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Graphiccards'

    def __str__(self):
        return f'{self.graphiccard_type}'


class Devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    barcode = models.ImageField(upload_to='images/', blank=True)
    device_type = models.ForeignKey(to=DeviceType, on_delete=models.RESTRICT)
    device_dns_name = models.CharField(max_length=30, blank=True, null=True)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.RESTRICT)
    device_model = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=30, blank=True, null=True)
    service_number = models.CharField(max_length=30, blank=True, null=True)
    mac_address = models.CharField(max_length=30, blank=True, null=True)
    ip_address = models.CharField(max_length=30, blank=True, null=True)
    device_user = models.ForeignKey(to=User, on_delete=models.RESTRICT, blank=True, null=True)
    processor_id = models.ForeignKey(to=Processors, on_delete=models.RESTRICT, blank=True, null=True)
    memory_id = models.ForeignKey(to=Memories, on_delete=models.RESTRICT, blank=True, null=True)
    harddisk_id = models.ForeignKey(to=Harddisks, on_delete=models.RESTRICT, blank=True, null=True)
    graphiccard_id = models.ForeignKey(to=Graphiccards, on_delete=models.RESTRICT, blank=True, null=True)
    in_use = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Devices'

    def __str__(self):
        return f'{self.barcode} {self.device_type.device_type_name} {self.manufacturer.manufacturer_name} ' \
               f'{self.device_model}'

    def save(self, *args, **kwargs):
        if self.device_user:
            self.in_use = True
        else:
            self.in_use = False
        return super(Devices, self).save(*args, **kwargs)
