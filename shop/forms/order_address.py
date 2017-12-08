from django import forms

from shop.models import Address


class OrderAddressForm(forms.Form):

    CNT_COMM = {
        'class': 'form-control col-sm-2',
        'id': 'comment'
    }

    CNT_ADD = {
        'class': 'form-control col-sm-2',
        'id': 'send_address'
    }

    CNT_INV_ADD = {
        'class': 'form-control col-sm-2',
        'id': 'invoice_address'
    }

    comments = forms.CharField(label='Comment to order:',
                               widget=forms.Textarea(attrs=CNT_COMM))
    send_address = forms.CharField(label='Send address',
                                   widget=forms.Select(attrs=CNT_ADD))
    bill_address = forms.CharField(label='Bill address:',
                                   widget=forms.Select(attrs=CNT_INV_ADD))

    def __init__(self, user, *args, **kwargs):
        choice = []
        addresses = Address.objects.filter(user=user)
        for address in addresses:
            choice.append((address.id, address))
        super(OrderAddressForm, self).__init__(*args, **kwargs)
        self.fields['send_address'].widget.choices = choice
        self.fields['bill_address'].widget.choices = choice
