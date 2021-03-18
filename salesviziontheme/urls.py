from django.urls import path
from .views import IndexView as theme


urlpatterns = [
    path('', theme.home, name = 'home'),
    path('contact/', theme.contact, name='contact'),
]