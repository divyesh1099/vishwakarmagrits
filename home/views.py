from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
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

def my_login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "home/login.html", {
                "error": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")

@login_required
def my_logout(request):
    logout(request)
    return redirect("/")

def my_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["password2"]
        if password != confirmation:
            return render(request, "home/signup.html", {
                "error": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.set_password(password)
            user.is_active=True
            user.is_staff=True
            user.save()
        except IntegrityError:
            return render(request, "home/signup.html", {
                "error": "Username already taken."
            })
        login(request, user)
        return redirect("/")
    else:
        return render(request, "home/signup.html")

@login_required
def view_profile(request):
    try:
        profile = Profile.objects.get_or_create(user = request.user)[0]
    except Exception as e:
        print("Following error occured :", e)
    return render(request, 'home/view_profile.html')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        try:
            profile = Profile.objects.get_or_create(user = request.user)[0]
        except Exception as e:
            print("Following error occured :", e)
        if request.FILES:
            image = request.FILES["image"]
            profile.image = image
            profile.save()
        if request.POST["username"]:
            username = request.POST["username"]
            user.username = username
            user.save()
        if request.POST["email"]:
            email = request.POST["email"]
            user.email = email
            user.save()
        return render(request, 'home/view_profile.html')
        
    else:
        profile = Profile.objects.get_or_create(user = request.user)[0]
        context = {
            "profile":profile
        }
        return render(request, 'home/edit_profile.html', context)

@login_required
def delete_profile(request):
    try:
        user = User.objects.get(username = request.user.username)
        user.delete()
    except Exception as e:
        print("User delete error is ", e)
        logout(request)
        return render(request, 'home/login.html')
    return redirect("/")