from django import forms
from django.core.validators import EmailValidator

from shop.models import Product, Order, Invoice


class LoginForm(forms.Form):
    CNT_ID = {
        'class': 'form-control col-sm-2',
        'id': 'login'
    }

    CNT_PASSWORD = {
        'class': 'form-control col-sm-2',
        'id': 'pass'
    }

    username = forms.CharField(label="Username", widget=forms.TextInput(attrs=CNT_ID))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs=CNT_PASSWORD))


class RegisterForm(forms.Form):
    CNT_USERNAME = {
        'class': 'form-control col-sm-4',
        'id': 'login',
    }
    CNT_EMAIL = {
        'class': 'form-control col-sm-4',
        'id': 'email'
    }
    CNT_PASSWORD_1 = {
        'class': 'form-control col-sm-4',
        'id': 'pass'
    }

    CNT_PASSWORD_2 = {
        'class': 'form-control col-sm-4',
        'id': 'pass_check'
    }

    username = forms.CharField(label="Username", widget=forms.TextInput(attrs=CNT_USERNAME))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs=CNT_EMAIL), validators=[EmailValidator()])
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs=CNT_PASSWORD_1))
    password_checked = forms.CharField(label="Re-enter password", widget=forms.PasswordInput(attrs=CNT_PASSWORD_2))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_checked")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password's don't match!"
            )


class ChangePasswordForm(forms.Form):
    CNT_PASSWORD = {
        'class': 'form-control col-sm-4',

    }

    password_old = forms.CharField(label="Old password", widget=forms.PasswordInput(attrs=CNT_PASSWORD))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs=CNT_PASSWORD))
    password_checked = forms.CharField(label="Re-enter password", widget=forms.PasswordInput(attrs=CNT_PASSWORD))

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_checked")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password's don't match!"
            )


class ProductQuantityForm(forms.Form):

    CNT_QUANTITY = {
        'name': "quantity",
        'min': "1",
        'step': "1",
        'value':  "1",
        'class': "form-control input-sm col-sm-4 quantity_product",
    }

    quantity = forms.IntegerField(label="", widget=forms.NumberInput(attrs=CNT_QUANTITY))


class ProductAvailabilityForm(forms.ModelForm):
    CNT_QUANTITY = {
        'name': "quantity",
        'min': "0",
        'step': "1",
        'value': "0",
        'class': "form-control col-sm-4",
    }

    quantity = forms.IntegerField(label="Quantity available", widget=forms.NumberInput(attrs=CNT_QUANTITY))

    class Meta:
        model = Product
        fields = '__all__'


class ContactForm(forms.Form):
    CNT_NAME = {
        'name': 'first_name'
    }

    CNT_EMAIL = {
        'name': "email"
    }

    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs=CNT_NAME))
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs=CNT_EMAIL))
    content = forms.CharField(required=True, widget=forms.Textarea)


class OrderAddressForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('comments', 'send_address')


class InvoiceAddressForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('bill_address',)

