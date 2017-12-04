from django import forms


class ContactForm(forms.Form):
    CNT_NAME = {
        'name': 'first_name'
    }

    CNT_EMAIL = {
        'name': "email"
    }

    contact_name = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs=CNT_NAME))
    contact_email = forms.EmailField(required=True,
                                     widget=forms.EmailInput(attrs=CNT_EMAIL))
    content = forms.CharField(required=True,
                              widget=forms.Textarea)
