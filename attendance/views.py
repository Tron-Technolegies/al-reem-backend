from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Device, DeviceUserMap, Employee, AttendanceLog
from .serializers import AttendanceInSerializer
from django.utils.dateparse import parse_datetime

class DeviceAttendanceAPI(APIView):
    # Simple API-key style validation (X-Device-Token header)
    def post(self, request):
        token = request.headers.get("X-Device-Token")
        if not token:
            return Response({"detail":"missing token"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            device = Device.objects.get(api_token=token, enabled=True)
        except Device.DoesNotExist:
            return Response({"detail":"invalid token"}, status=status.HTTP_403_FORBIDDEN)

        serializer = AttendanceInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # try to map employee
        employee = None
        if data.get("employee_code"):
            try:
                employee = Employee.objects.get(employee_code=data["employee_code"])
            except Employee.DoesNotExist:
                employee = None
        elif data.get("device_user_id"):
            try:
                mapping = DeviceUserMap.objects.get(device=device, device_user_id=data["device_user_id"])
                employee = mapping.employee
            except DeviceUserMap.DoesNotExist:
                employee = None

        # idempotency: create only if device+event_id not exists
        obj, created = AttendanceLog.objects.get_or_create(
            device=device,
            device_event_id=data["device_event_id"],
            defaults={
                "employee": employee,
                "timestamp": data["timestamp"],
                "status": data["status"],
                "raw_payload": data.get("raw_payload", {})
            }
        )
        if not created:
            return Response({"detail":"already exists"}, status=status.HTTP_200_OK)
        return Response({"detail":"saved"}, status=status.HTTP_201_CREATED)
