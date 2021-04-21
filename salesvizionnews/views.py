from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .models import question, answer
from django.http import Http404
import datetime


class IndexView(TemplateView):

    template_name = 'Mark Steele News'

    def news(request):
        return render(request, 'news/news.html')