from django.db import models

class Employee(models.Model):
    employee_code = models.CharField(max_length=64, unique=True)  # your HR id
    name = models.CharField(max_length=200)
   

    def __str__(self): return f"{self.employee_code} - {self.name}"

class Device(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    port = models.IntegerField(default=80)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # store safely in prod (secrets)
    device_type = models.CharField(max_length=50)  # e.g. 'hikvision'
    api_token = models.CharField(max_length=128, blank=True, null=True)  # optional
    enabled = models.BooleanField(default=True)

    def base_url(self):
        return f"http://{self.ip}:{self.port}"

class DeviceUserMap(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    device_user_id = models.CharField(max_length=128)  # id used on device
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("device", "device_user_id")

class AttendanceLog(models.Model):
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    device_event_id = models.CharField(max_length=200)  # unique id from device (if any)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=32, choices=[("checkin","checkin"),("checkout","checkout"),("unknown","unknown")])
    raw_payload = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = ("device", "device_event_id")  # prevents duplicates
