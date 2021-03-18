from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class loginForm(forms.Form):
    username = forms.CharField(label="What's Your Username?",
        error_messages = {'required' : 'Enter a valid Username.'},
        max_length = 100,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Username'
            })
    )

    password = forms.CharField(label = "What's Your Password?",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 100,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Password'
            })
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        if not User.objects.filter(username = data).exists():
            raise ValidationError("Username Dosen't Match")
        return data

# class registerForm(forms.Form):

