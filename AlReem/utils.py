from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import json
import os

from django.conf import settings

def generate_invoice_pdf(order):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
    elements = []
    styles = getSampleStyleSheet()

   
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'Handcar_logo.png')

    if os.path.exists(logo_path):
        img = Image(logo_path, width=150, height=60)
        elements.append(img)
    else:
        print("Error: Logo not found at:", logo_path)

    elements.append(Spacer(1, 20))

   
    elements.append(Paragraph("Invoice - Handcar", styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"<b>Order ID:</b> {order.order_id}", styles['Normal']))
    elements.append(Paragraph(f"<b>Customer:</b> {order.user.username}", styles['Normal']))
    elements.append(Paragraph(f"<b>Address:</b> {order.address}", styles['Normal']))
    elements.append(Paragraph(f"<b>Date:</b> {order.created_at.strftime('%d-%m-%Y')}", styles['Normal']))
    elements.append(Spacer(1, 16))

   
    try:
        products = json.loads(order.products)
        data = [['Product', 'Quantity', 'Price (AED)', 'Subtotal (AED)']]  # Table header
        total = 0

        for product in products:
            quantity = product['quantity']
            price = float(product['price'])
            subtotal = quantity * price
            total += subtotal
            data.append([
                Paragraph(product['name'], styles['Normal']),
                quantity,
                f"{price:.2f}",
                f"{subtotal:.2f}"
            ])

        # Add discount row if applicable
        if order.coupon:
            coupon_data = json.loads(order.coupon)
            discount_amount = float(coupon_data.get('discount_amount', 0))
            data.append(['', '', 'Discount:', f"-{discount_amount:.2f}"])
            total -= discount_amount

        # Add total row
        data.append(['', '', 'Total:', f"AED {total:.2f}"])

        # Adjusted column widths for better spacing
        col_widths = [200, 80, 100, 100]

        table = Table(data, colWidths=col_widths, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f2f2f2")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        elements.append(table)
    except Exception as e:
        elements.append(Paragraph(f"<b>Error loading products:</b> {str(e)}", styles['Normal']))

   
    elements.append(Spacer(1, 30))
    elements.append(Paragraph("<i>Thank you for shopping with Handcar! </i>", styles['Italic']))

    doc.build(elements)
    buffer.seek(0)
    return buffer