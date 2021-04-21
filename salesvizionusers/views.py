from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import loginForm, registerForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
# from .token import generate_token
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
from django.utils.html import strip_tags
from django.contrib.auth import update_session_auth_hash


class IndexView(TemplateView):

    template_name = 'Mark Steele Users'

    def register(request):
        if request.user.is_authenticated:
            return redirect('profile')
        
        elif request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                
                newUser = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password)
                newUser.is_active = False
                newUser.save()

                # current_site = get_current_site(request)
                # email_subject = 'Account Activation Link for Salesvizion.com'

                # finalEmail = render_to_string('activeaccount/activate.html',
                #             {'user': firstName,
                #             'domain': current_site.domain,
                #             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                #             'token': generate_token.make_token(user)})

                # email_message = strip_tags(finalEmail)
                # main_email = EmailMultiAlternatives(
                #     email_subject,
                #     email_message,
                #     settings.EMAIL_HOST_USER,
                #     [email],
                # )
                # main_email.attach_alternative(finalEmail, "text/html")
                # main_email.send()

                messages.success(request, 'Thank You For Registration. Please check your email to activate your account. Thanks')
                return redirect('register')

        else:
            form = registerForm()

        return render(request, 'users/register.html', {'form':form})

    # def ActivateAccountView(request, uidb64, token):
    #     if request.user.is_authenticated:
    #         return redirect('profile')
        
    #     else:
    #         try:
    #             uid = force_text(urlsafe_base64_decode(uidb64))
    #             user = User.objects.get(pk=uid)

    #         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
    #             user = None

    #         if user is not None and generate_token.check_token(user, token):
    #             user.is_active = True
    #             user.save()
    #             return render(request, 'activeaccount/activate_success.html')

    #         elif not generate_token.check_token(user, token):
    #             return render(request, 'activeaccount/account_already_active.html')

    #         else:
    #             return render(request, 'activeaccount/activate_failed.html')

    def login(request):
        if request.user.is_authenticated:
            return redirect('profile')

        elif request.method == 'POST':
            form = loginForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                if User.objects.get(username=username).is_active:
                    user = auth.authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        request.session['usernameAll'] = username
                        if 'next' in request.POST:
                            return redirect(request.POST.get('next'))

                        else:
                            return redirect('profile')              

                    else:
                        messages.error(request, "Password Dosen't Match")
                        return redirect('login')
                else:
                    messages.error(request, 'Your Account Is Not Activated.')
                    return redirect('login')
        else:
            form = loginForm()

        return render(request, 'users/login.html', {'form':form})


    def logout(request):
        auth.logout(request)
        return redirect('login')
    
    @login_required
    def profile(request):        
        return render(request, 'users/profile.html')
