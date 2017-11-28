from django import forms


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
