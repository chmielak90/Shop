from django import forms

from shop.models import Order


class OrderAddressForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('comments', 'send_address')
