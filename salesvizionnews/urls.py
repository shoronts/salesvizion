from django.urls import path
from .views import IndexView as news


urlpatterns = [
    path('news/', news.news, name = 'news'),
]