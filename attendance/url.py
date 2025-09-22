from django.urls import path
from .views import DeviceAttendanceAPI

urlpatterns = [
    path("api/device/attendance/", DeviceAttendanceAPI.as_view(), name="device-attendance"),
]
