from django.db import models

from members.models import Member

# Create your models here.
class Invoice(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="invoices")
    invoice_number = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Plan amount or total fee
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)   # This invoice payment
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)    # Remaining due after this invoice

    payment_method = models.CharField(
        max_length=20,
        choices=[("cash", "Cash"), ("upi", "UPI"), ("card", "Card"), ("bank", "Bank Transfer")],
        default="cash"
    )

    remarks = models.TextField(blank=True, null=True)

