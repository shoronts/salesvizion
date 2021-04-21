from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import contactForm
from django.core.mail import send_mail


class IndexView(TemplateView):

    template_name = 'Mark Steele Theme'

    def home(request):
        return render(request, 'theme/home.html')

    def contact(request):
        if request.method == 'POST':
            form = contactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']

                mail = (
                        'My name is ' + name + ',' +
                        ' My Email is ' + email + ',' +
                        ' My Subject is ' + subject + ',' +
                        ' My message is ' + message)
                print('shoron')
                send_mail(
                    'Message from Salesvizion.com',
                    mail,
                    'webmaster@salesvizion.com',
                    ['mdshariffoysalshoron@gmail.com'],
                    fail_silently=False,)

                print('shoron1')

                messages.success(request, 'Thank you for your inquiry! We will get back to you within 48 hours.')
                return redirect ('contact')

        else:
            form = contactForm()

        return render(request, 'theme/contact.html', {'form' : form})
