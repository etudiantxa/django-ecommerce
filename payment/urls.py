from django.urls import path
from . import views

urlpatterns = [
    path('payment-process/', views.payment_process, name='payment-process',),

]
