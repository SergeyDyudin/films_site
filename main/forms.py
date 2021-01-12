from django import forms


class LoginForm(forms.Form):
    username = forms.TextInput(attrs={'placeholder': 'Username'})
    password = forms.PasswordInput(attrs={'placeholder': 'Password'})
