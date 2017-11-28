from django import forms
from django.core.validators import EmailValidator


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
            raise forms.ValidationError("Password's don't match!")
