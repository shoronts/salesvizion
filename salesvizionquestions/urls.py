from django.urls import path
from .views import IndexView as questions


urlpatterns = [
    path('questions/', questions.question, name = 'question'),
    path('questions/<slug>', questions.allquestion, name='allquestion'),
    path('results/', questions.result, name='results'),
    path('results/<slug>/', questions.singleresult, name='singleresults'),
    path('cancel-exam/', questions.cancelexam, name='cancelexam'),
]