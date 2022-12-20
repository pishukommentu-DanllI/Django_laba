from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView



class SingUp(CreateView):
    form_class = UserCreationForm
    template_name = 'films/SingUp.html'  # ссылка на шаблон (где хранится это html)
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form, 'title': 'Registr'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Log(LoginView):
    form_class = AuthenticationForm
    template_name = 'films/Login.html/'
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        return {'form': form, 'title': 'Log'}




def Logout(request):
    logout(request)
    return redirect('home')