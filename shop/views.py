from multiprocessing import context
from re import I
from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from numpy import product

from cart.forms import CartAddProductForm
from .models import Cathegory, Produit
from django.db.models import Q

def index(request):
    products = Produit.objects.all()
    context = {'title': 'Bienvenue chez Xarala', 'products': products}
    return render(request, "index.html", context)


class ProductList(ListView):
    #model = Produit
    #context_object_name = "products"
    template_name = "shop/produit_list.html"

    def get(self, request):
        products = Produit.objects.all()
        cathegories = Cathegory.objects.all()
        q = request.GET.get("q")
        request.session["nom"] = "Xarala"
        request.session.get("nom")
        del request.session["nom"] 
        print("Query", q)
        if q:
            products = Produit.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(cathegory__name__icontains=q)
                )
        return render(request, self.template_name, {'products': products, 'cathegories': cathegories})

        

class ProductDetail(DetailView):
    model = Produit
    context_object_name = "product"
    # def get(self, request):
      #  return render(request, self.template_name, {"product":product})
      
    template_name = "shop/produit_detail.html"
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["cart_product_form"] = CartAddProductForm()
        return context

