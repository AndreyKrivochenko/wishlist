from django import forms
from django.core.exceptions import ValidationError

from .models import Product, WishList


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'link', 'price')

    def clean_title(self):
        data = self.cleaned_data['title']

        if Product.objects.filter(title=data).exists():
            raise ValidationError('Такая запись уже существует')

        return data
