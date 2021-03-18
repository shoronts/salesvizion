from django import forms
from django.core.exceptions import ValidationError


class contactForm(forms.Form):
    name = forms.CharField(error_messages = {'required' : 'Please enter your name.'},
        widget = forms.TextInput( attrs = {
            'placeholder' : 'Name'
        })
    )

    email = forms.EmailField(error_messages={'required' : 'Please use A Vaild Email.'},
        widget = forms.EmailInput( attrs = {
            'placeholder' : 'Email'
        })
    )

    url = forms.URLField(error_messages = {'required' : 'Please enter your website URL'},
        widget = forms.URLInput( attrs = {
            'placeholder' : 'Business URL or description'
        })
    )

    message = forms.CharField(error_messages = {'required' : 'Your Message Is Important For Us.'},
        widget = forms.Textarea( attrs = {
            'placeholder' : 'How can we help your business thrive?',
            'rows' : 5
        })
    )
