"""Management_It URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from device_management import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('device', views.DevicesView, basename='devices')
#router.register('devices/<int:device-id>', views.DevicesView, basename='devicessingle')

urlpatterns = [
    path('api/', include(router.urls)),
]