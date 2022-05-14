from distutils.command import upload
from unicodedata import name
from django.db import models
from matplotlib import image
from numpy import True_
from django.urls import reverse

class Cathegory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class  Meta:
        verbose_name_plural = 'cathegories'

    def __str__(self):
        return self.name    


class Produit(models.Model):
    cathegory = models.ForeignKey(Cathegory, related_name="products", on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

def get_absolute_url(self):
    return reverse("product-details", kwargs={"slug": self.slug})




