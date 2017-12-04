from django import forms


class ProductQuantityForm(forms.Form):

    CNT_QUANTITY = {
        'name': "quantity",
        'min': "1",
        'step': "1",
        'value':  "1",
        'class': "form-control input-sm col-sm-4 quantity_product",
    }

    quantity = forms.IntegerField(label="",
                                  widget=forms.NumberInput(attrs=CNT_QUANTITY))
