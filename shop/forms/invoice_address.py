from django import forms

from shop.models import Address


class InvoiceAddressForm(forms.Form):

    CHOICE = []
    addresses = Address.objects.all()
    for address in addresses:
        CHOICE.append((address.id, address))

    CNT_ADD = {
        'class': 'form-control col-sm-2',
        'id': 'invoice_address'
    }

    bill_address = forms.CharField(label='Invoice address:',
                                   widget=forms.Select(attrs=CNT_ADD,
                                                       choices=CHOICE))
