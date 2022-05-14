
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

def send_new_order_email(email):
    send_mail(
        'votre commande sur mangane',
        'nous avons bien recus votre commande',
        'contact@mangane.com',
        [email],
        fail_silently=False,
    )

def send_new_order_email_with_template(email):
    template = get_template("email/new-order.html")
    context = {"email": email}
    subject, from_email = ("nouvelle commande sur mangane", "contact@mangane.com")
    body = template.render(context)
    message = EmailMultiAlternatives(subject, body, from_email, [email])
    message.attach_alternative(body, "text/html")
    message.send(fail_silently=False)

def payment_successful_email(email):
    send_mail(
        'votre commande sur mangane',
        'nous avons bien recus votre paiement',
        'contact@mangane.com',
        [email],
        fail_silently=False,
    )
