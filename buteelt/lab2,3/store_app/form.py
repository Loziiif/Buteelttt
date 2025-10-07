from django import forms
from .models import Angilal, Baraa

class Form(forms.ModelForm):
    class Meta:
        model = Baraa
        fields = ['bname', 'angilal']
        labels = {
            'bname': 'Барааны нэр',
            'angilal': 'Ангилал'
        }