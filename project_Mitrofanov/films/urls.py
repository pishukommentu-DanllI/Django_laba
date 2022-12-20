from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('add/', form, name='Form'),
    path('edit/<int:id>/', Edit, name='edit'),
    path('delete/<int:id>/', Delete, name='delete'),

]