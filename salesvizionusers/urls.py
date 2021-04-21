from django.urls import path
from .views import IndexView as users


urlpatterns = [
    path('register/', users.register, name='register'),
    path('login/', users.login, name='login'),
    path('logout/', users.logout, name = 'logout'),
    path('profile/', users.profile, name = 'profile'),
]