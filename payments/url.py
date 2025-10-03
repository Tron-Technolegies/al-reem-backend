from django.urls import path
from payments import views


urlpatterns = [
    path("all_invoices", views.all_invoices, name="all_invoices"),
    path("invoice_member/<int:member_id>/", views.member_invoices, name="member_invoices"),
]