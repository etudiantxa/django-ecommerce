from lib2to3.pgen2 import token
from unicodedata import name
from urllib import response

from django.http import HttpResponse
from send_mail.views import payment_successful_email
import paydunya
from paydunya import InvoiceItem, Store, Invoice
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from orders.models import Order

paydunya.debug = True

paydunya.api_keys = settings.PAYDUNYA_ACCESS_TOKENS
store = Store(name="magasin chez mangane")

def payment_process(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, pk=order_id)
    order_items = order.items.all()
    items =[InvoiceItem(
        name=item.product.name,
        quantity=item.quantity,
        unit_price=str(item.price),
        total_price=str(item.price*item.quantity),
        description=item.product.name
    ) for item in order_items]
    invoice = paydunya.Invoice(store)
    invoice.add_items(items)
    successful, response = invoice.create()
    if successful:
        # envoi un mail, nous avons recu votre commande
        
        return redirect(response.get("response_text"))





