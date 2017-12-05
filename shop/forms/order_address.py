from django import forms

from shop.models import Address


class OrderAddressForm(forms.Form):

    CHOICE = []
    addresses = Address.objects.all()
    for address in addresses:
        CHOICE.append((address.id, address))

    CNT_COMM = {
        'class': 'form-control col-sm-2',
        'id': 'comm'
    }

    CNT_ADD = {
        'class': 'form-control col-sm-2',
        'id': 'send_address'
    }

    comments = forms.CharField(label='Comment to order:',
                               widget=forms.Textarea(attrs=CNT_COMM))
    send_address = forms.CharField(label='Send address:',
                                   widget=forms.Select(attrs=CNT_ADD,
                                                       choices=CHOICE))
