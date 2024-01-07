from django.forms import ModelForm
from django import forms
from .models import Product, OrderItem

class ProductForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Product
        fields = "__all__"

class OrderForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"