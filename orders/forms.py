from .models import Order
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1', 'address_line_2', 'country', 'state', 'city', 'order_note']
        fields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1', 'order_note']
