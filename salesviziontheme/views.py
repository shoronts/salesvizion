from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import contactForm


class IndexView(TemplateView):

    template_name = 'Mark Steele Theme'

    def home(request):
        return render(request, 'theme/home.html')

    def contact(request):
        form = contactForm()

        if request.method == 'POST':
            form = contactForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Thank you for your inquiry! We will get back to you within 48 hours.')
                return redirect ('contact')

        else:
            form = contactForm()

        return render(request, 'theme/contact.html', {'form' : form})
