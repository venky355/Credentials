# forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'country', 'quantity', 'price', 'image', 'dealer']
