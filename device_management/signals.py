from io import BytesIO

import barcode
from barcode.writer import ImageWriter
from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver

from device_management.models import Devices


@receiver(post_save, sender=Devices)
def create_barcode(sender, instance, **kwargs):
    if not instance.barcode:
        code39_string = f'{instance.device_id}{instance.device_type.device_type_shortcut}' \
                        f'{instance.device_type_id}-{instance.serial_number[-4:]}'
        CODE39 = barcode.get_barcode_class('code39')
        code39 = CODE39(code39_string, writer=ImageWriter())
        buffer = BytesIO()
        code39.write(buffer)
        instance.barcode.save(f'{code39_string}.png', File(buffer))