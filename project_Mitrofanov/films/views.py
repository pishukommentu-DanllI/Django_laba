from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from .models import Category, Films


def index(request):
    create_Category()
    return render(request, 'films/index.html', {'films': Films.objects.all()})


def form(request):
    if request.method == 'POST':
        form = Order_form(request.POST)

        if form.is_valid():

            Category_id = form.cleaned_data['Category']
            Category_ids = Category.objects.filter(id__in=Category_id)


            films_obj = Films.objects.create(
                name=form.cleaned_data['name'],
                # date_made=form.cleaned_data['date_made'],
                date_show=form.cleaned_data['date_show'],
                acteru=form.cleaned_data['acteru'],
            )

            films_obj.category.set(Category_ids, through_defaults={})

            return redirect('home')

        else:
            print('is_not_valid')
    else:
        form = Order_form()

    return render(request, 'films/form.html', {'form': form})


def Edit(request, id):
    if request.method == 'POST':
        form = Order_form(request.POST)

        if form.is_valid():

            Category_id = form.cleaned_data['Category']
            Category_ids = Category.objects.filter(id__in=Category_id)

            films_obj = Films.objects.get(id=id)

            films_obj.name = form.cleaned_data['name']
            films_obj.date_show = form.cleaned_data['date_show']
            films_obj.acteru = form.cleaned_data['acteru']

            films_obj.category.set(Category_ids, through_defaults={})

            films_obj.save()
            return redirect('home')

        else:
            print('is_not_valid')
    else:
        form = Order_form()

    return render(request, 'films/form.html', {'form': form})


def Delete(request, id):
    try:
        film = Films.objects.get(id=id)
    except:
        return HttpResponseNotFound('<h2>Person not found</h2>')
    film.delete()
    return redirect('home')



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


def profile(request):
    return reverse_lazy('home')


def Logout(request):
    logout(request)
    return redirect('home')



def create_Category():
    if Category.objects.all().count() == 0:
        Category.objects.create(name='fanastic')
        Category.objects.create(name='comedi')
        Category.objects.create(name='scream')
        Category.objects.create(name='ekesh')
