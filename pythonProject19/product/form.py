from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm , forms
from .models import *

class BuyForm(forms.Form):
    pass

class UserOrderForm(forms.Form):
    pass

class AddProductForm(forms.ModelForm):

    category_name = forms.CharField(max_length=30, required=False)
    description = forms.CharField(max_length=100, required=False)
    buying_price= forms.IntegerField( required=False)
    selling_price = forms.IntegerField( required=False)
    purchase = forms.IntegerField( required=False)
    sale= forms.IntegerField( required=False)
    class Meta:
        model=Products
        fields=[
            'product_name',

            'category_name',
            'description',
            'buying_price',
            'selling_price',
            'purchase',
            'sale',
            'stock',

        ]

class InvoiceForm(forms.ModelForm):

    class Meta:
        model=Invoice
        fields=[
            'customer',
            'product',
            'total_price',
            'delivery_charge',
            'discount',
            'payment',
            'due',

        ]

class ClothesForm(forms.ModelForm):

    class Meta:
        model=Products
        fields=[
            'purchase',
            'sale',
        ]



class ElectronicsForm(forms.ModelForm):

    class Meta:
        model=Products
        fields=[
            'purchase',
            'sale',
        ]

class FoodForm(forms.ModelForm):

    class Meta:
        model=Products
        fields=[
            'purchase',
            'sale',
        ]