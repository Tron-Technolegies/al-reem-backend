from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import JsonResponse

from members.models import Member
from .models import Invoice
from django.views.decorators.csrf import csrf_exempt

def all_invoices(request):
    invoices = Invoice.objects.select_related("member").all()
    data = [
        {
            "invoice_number": inv.invoice_number,
            "member": inv.member.name,  # assuming Member has a 'name' field
            "date": inv.date,
            "total_amount": float(inv.total_amount),
            "paid_amount": float(inv.paid_amount),
            "due_amount": float(inv.due_amount),
            "payment_method": inv.payment_method,
            "remarks": inv.remarks,
        }
        for inv in invoices
    ]
    return JsonResponse(data, safe=False)


# 2) View invoices of a specific member
def member_invoices(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    invoices = member.invoices.all()  # thanks to related_name="invoices"
    data = [
        {
            "invoice_number": inv.invoice_number,
            "date": inv.date,
            "total_amount": float(inv.total_amount),
            "paid_amount": float(inv.paid_amount),
            "due_amount": float(inv.due_amount),
            "payment_method": inv.payment_method,
            "remarks": inv.remarks,
        }
        for inv in invoices
    ]
    return JsonResponse({"member": member.name, "invoices": data})