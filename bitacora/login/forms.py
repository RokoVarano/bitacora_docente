from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length='50')
    password = forms.CharField(label='Clave', max_length=32, widget=forms.PasswordInput)

