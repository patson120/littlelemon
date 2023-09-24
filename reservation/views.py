from django.shortcuts import render
from . import models

# Create your views here.


def home(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'menu.html')

def menu(request):
    menu_data = models.Menu.objects.all()
    main_data = dict(menu=menu_data)
    return render(request, 'menu.html', dict(menu=main_data))

def display_menu_item(request):
    return render(request, 'menu.html')