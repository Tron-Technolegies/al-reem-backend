from rest_framework import serializers
from .models import AttendanceLog, Device, Employee

class AttendanceInSerializer(serializers.Serializer):
    device_id = serializers.IntegerField()
    device_event_id = serializers.CharField()
    device_user_id = serializers.CharField(allow_null=True, required=False)
    employee_code = serializers.CharField(allow_null=True, required=False)
    timestamp = serializers.DateTimeField()
    status = serializers.ChoiceField(choices=["checkin","checkout","unknown"])
    raw_payload = serializers.DictField(child=serializers.JSONField(), required=False)
