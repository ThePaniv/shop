from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=12)
    message = forms.CharField(max_length=5000)

