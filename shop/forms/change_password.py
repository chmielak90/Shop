from django import forms


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
            raise forms.ValidationError("Password's don't match!")
