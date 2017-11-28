from django import forms

from shop.models import Invoice


class InvoiceAddressForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('bill_address',)
