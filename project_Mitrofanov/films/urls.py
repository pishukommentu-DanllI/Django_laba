from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('SingUp', SingUp.as_view(), name='SingUp'),
    path('Login', Log.as_view(), name='Login'),
    path('Logout', Logout, name='Logout'),
    path('add/', form, name='Form'),
    path('edit/<int:id>/', Edit, name='edit'),
    path('delete/<int:id>/', Delete, name='delete'),

]