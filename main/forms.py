from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField( max_length = 20)
    clave = forms.CharField( min_length = 6, max_length = 30)
