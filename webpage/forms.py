from django import forms
from .models import ProductList

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductList
        fields = ['stall_owner', 'product_id', 'product_image', 'product_name', 'product_price', 'stocks']
