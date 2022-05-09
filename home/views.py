from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    meals = Meal.objects.all()
    context = {
        "meals": meals,
    }
    return render(request, 'home/index.html', context)

def meal(request, type):
    meal = Meal.objects.get(type = type)
    context = {
        "meal": meal
    }
    return render(request, 'home/meal.html', context)

def item(request, name):
    item = Item.objects.get(name = name)
    context = {
        "item": item
    }
    return render(request, 'home/item.html', context)
