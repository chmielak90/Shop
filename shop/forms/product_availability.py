from django import forms

from shop.models import Product


class ProductAvailabilityForm(forms.ModelForm):
    CNT_QUANTITY = {
        'name': "quantity",
        'min': "0",
        'step': "1",
        'value': "0",
        'class': "form-control col-sm-4",
    }

    quantity = forms.IntegerField(label="Quantity available",
                                  widget=forms.NumberInput(attrs=CNT_QUANTITY))

    class Meta:
        model = Product
        fields = '__all__'
