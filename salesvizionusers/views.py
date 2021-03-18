from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import loginForm


class IndexView(TemplateView):

    template_name = 'Mark Steele Users'

    def register(request):
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request, 'users/register.html')

    def login(request):
        form = loginForm()
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
