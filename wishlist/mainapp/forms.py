from django import forms
from django.forms import fields

from .models import Product, WishList


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'link', 'price')