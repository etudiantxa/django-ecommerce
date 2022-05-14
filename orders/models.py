from django.db import models
from shop.models import Produit

class Order(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=60)
    paid = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def get_total_cost(self):
        get_total = sum(item.get_cost() for item in self.items.all())
        return get_total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE,)
    product = models.ForeignKey(Produit, related_name="order_items", on_delete=models.CASCADE,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price*self.quantity    


