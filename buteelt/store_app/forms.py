from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'price', 'stock']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Барааны нэр'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Тайлбар'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Үнэ'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Нөөц'}),
        }
