from django.urls import path, include
from .views import *
urlpatterns = [
    path('SingUp', SingUp.as_view(), name='SingUp'),
    path('Login', Log.as_view(), name='Login'),
    path('Logout', Logout, name='Logout'),

]