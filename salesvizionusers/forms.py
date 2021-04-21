from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class loginForm(forms.Form):
    username = forms.CharField(label="What's Your Username?",
        error_messages = {'required' : 'Enter a valid Username.'},
        max_length = 100,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Username',
            'class' : 'form-control'
            })
    )

    password = forms.CharField(label = "What's Your Password?",
        error_messages = {'required' : 'Passwords can’t be nothing.'},
        min_length = 8,
        max_length = 100,
        widget = forms.PasswordInput(attrs = {
            'placeholder' : 'Password',
            'class' : 'form-control'
            })
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        if not User.objects.filter(username = data).exists():
            raise ValidationError("Username Dosen't Match")
        return data

class registerForm(forms.Form):
    first_name = forms.CharField(label="What's Your First Name?",
        error_messages = {'required' : 'Enter Your First Name.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'First Name',
            'class' : 'form-control'
            })
    )

    last_name = forms.CharField(label="What's Your Last Name?",
        error_messages = {'required' : 'Enter Your Last Name.'},
        max_length = 50,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Last Name',
            'class' : 'form-control'
            })
    )

    email = forms.EmailField(label="What's Your Email?",
        help_text = "We will send a email to this email",
        error_messages = {'required' : 'Enter a valid Email.'},
        max_length = 30,
        widget = forms.EmailInput( attrs = {
            'placeholder' : 'Email',
            'class' : 'form-control'
            })
    )

    username = forms.CharField(label="What's Your Username?",
        help_text = "Your login name",
        error_messages = {'required' : 'Enter a valid Username.'},
        max_length = 100,
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Username',
            'class' : 'form-control'
            })
    )

    password = forms.CharField(label="What's Your Password?",
        error_messages = {'required' : 'Enter a Secure Password.'},
        max_length = 50,
        min_length = 8,
        widget = forms.PasswordInput( attrs = {
            'placeholder' : 'Password',
            'class' : 'form-control'
            })
    )

    confirm_password = forms.CharField(label="What's Your Password?",
        error_messages = {'required' : 'Enter a Secure Password.'},
        max_length = 50,
        min_length = 8,
        widget = forms.PasswordInput( attrs = {
            'placeholder' : 'Confirm Password',
            'class' : 'form-control'
            })
    )

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email = data).exists():
            raise ValidationError("This email already exists.")
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username = data).exists():
            raise ValidationError("This uaername already exists.")
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                error = "Password Did not Match!!"
                self.add_error('password', error)
                self.add_error('confirm_password', error)
