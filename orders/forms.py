
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    full_name = forms.CharField(
        label="Nom Complet", widget=forms.TextInput({"class": "form-control", "placeholder": "Nom Complet"})
    )
    address = forms.CharField(
        label="Adresse de Livraison", widget=forms.TextInput({"class": "form-control", "placeholder": "Adresse de Livraison"})
    )
    email = forms.EmailField(
        label="Votre Email", widget=forms.TextInput({"class": "form-control", "placeholder": "Votre Email"})
    )
    phone = forms.CharField(
        label="Telephone", widget=forms.TextInput({"class": "form-control", "placeholder": "Telephone"})
    )
    

    class  Meta:
        model = Order
        fields = ( "full_name", "email", "phone", "address" )
        