from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import ListDevicesSerializer, DetailDeviceSerializer
from device_management import models


class DevicesView(viewsets.ReadOnlyModelViewSet):
    """
    Devices List lists all devices in the Company managed by the IT
    Devices Instance returns an object of the devices list
    """

    queryset = models.Devices.objects.all()
    serializer_class = ListDevicesSerializer

    def get_queryset(self):
        return self.queryset

    def get_object(self):
        device_id = self.kwargs.get('pk')
        return self.get_queryset().get(device_id=device_id)


    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except (models.Devices.DoesNotExist, KeyError):
            return Response({'error': 'Requested Device does not exist'}, status=status.HTTP_404_NOT_FOUND)
        self.serializer_class = DetailDeviceSerializer
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
