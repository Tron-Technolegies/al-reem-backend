# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=250, unique=True)  
    duration_days = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  



class Member(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, default=None)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=None)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Active")
    plan_type = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    total_fee = models.IntegerField(default=0)  
    due_amount = models.IntegerField(default=0) 
    joining_date = models.DateField(default=timezone.now)
    leave_date = models.DateField(blank=True, null=True)
    rejoin_date = models.DateField(blank=True, null=True)


class TrainerStaff(models.Model):
    STAFF_CHOICES = (
        ("trainer", "Trainer"),
        ("staff", "Staff"),
    )

    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    user = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=200, blank=True, null=True)
    trainer_or_staff = models.CharField(max_length=20, choices=STAFF_CHOICES)
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=5)
