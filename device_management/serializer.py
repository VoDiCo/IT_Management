from rest_framework import serializers
from device_management import models


class ListDevicesSerializer(serializers.ModelSerializer):
    """
    Serializes all Devices from models with modified fields
    """
    device_type_name = serializers.CharField(source='device_type.device_type_name')
    manufacturer = serializers.CharField(source='manufacturer.manufacturer_name')
    device_user_lastname = serializers.CharField(source='device_user.lname', allow_null=True)
    device_user_firstname = serializers.CharField(source='device_user.fname', allow_null=True)
    department = serializers.CharField(source='device_user.department.department_id', allow_null=True)

    class Meta:
        model = models.Devices
        fields = ['url',
                  'barcode',
                  'device_type_name',
                  'manufacturer',
                  'device_model',
                  'ip_address',
                  'mac_address',
                  'service_number',
                  'device_user_lastname',
                  'device_user_firstname',
                  'department',
                  'in_use',
                 ]

class DetailDeviceSerializer(serializers.ModelSerializer):
    """
    Serializes a spezific object(instance) from Device
    """

    class Meta:
        model = models.Devices
        fields = '__all__'
        depth = 2