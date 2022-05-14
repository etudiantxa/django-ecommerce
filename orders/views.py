from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from cart.models import Cart
from send_mail.views import send_new_order_email_with_template
from send_mail.views import send_new_order_email
from orders.models import OrderItem
from .forms import OrderCreateForm

def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            email = form.cleaned_data.get("email")
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
                cart.clear()
                request.session['order_id'] = order.id
                # on envoie un email au client
                #send_new_order_email(email)
                send_new_order_email_with_template(email)
                return redirect("payment-process")
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})

def order_created(request):
    return render(request, "orders/created.html")                
