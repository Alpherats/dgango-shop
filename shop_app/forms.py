from django import forms
from .models import ItemImg


class EditProduct(forms.ModelForm):
    class Meta:
        model = ItemImg
        fields = ['item', 'price', 'image']
