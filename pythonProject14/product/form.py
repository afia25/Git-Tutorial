from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm , forms
from .models import *

class BuyForm(forms.Form):
    pass

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=[
            'product_name',
            #'product_id',
            'buying_price',
            'selling_price',
        ]