from django import forms
from django.core.exceptions import ValidationError


class contactForm(forms.Form):
    name = forms.CharField(error_messages = {'required' : 'Please enter your Full Name.'},
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Full Name',
            'class' : 'form-control'
        })
    )

    email = forms.EmailField(error_messages={'required' : 'Please use A Vaild Email.'},
        widget = forms.EmailInput( attrs = {
            'placeholder' : 'Email',
            'class' : 'form-control'
        })
    )

    subject = forms.CharField(error_messages = {'required' : 'Please enter your Subject.'},
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Subject',
            'class' : 'form-control'
        })
    )
    

    message = forms.CharField(error_messages = {'required' : 'Your Message Is Important For Us.'},
        widget = forms.Textarea( attrs = {
            'class' : 'form-control',
            'placeholder' : 'How can we help your business thrive?',
            'rows' : 6
        })
    )
