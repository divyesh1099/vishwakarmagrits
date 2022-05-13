from re import M
from django.db import models
from django.contrib.auth.models import User
from requests import request

# Create your models here.

types_choices = (
    ("Breakfast" , "breakfast"),
    ("Lunch" , "lunch"),
    ("Dinner" , "dinner"),
)

class Meal(models.Model):
    type = models.CharField(max_length=100, choices=types_choices)
    image = models.ImageField(upload_to = "meals/%Y/%m/%d/", default = "meals/default.png")
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.type + " for " + str(self.date) + " " + str(self.time)


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="items")
    image = models.ImageField(upload_to = "items/%Y/%m/%d/", default = "items/default.png")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'user/profile/default_user.jpg', upload_to = 'user/profile/%Y/%m/%d/')
    
    def __str__(self):
        return self.user.username

class MyMeal(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False, blank=True)    
    mymeal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="mymeals")

    def __str__(self):
        return self.mymeal.type + " for " + str(self.mymeal.date) + " " + str(self.mymeal.time)

# class UserMeal(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     meal = models.ForeignKey(MyMeal, on_delete=models.CASCADE, related_name="usermeals")

#     def __str__(self):
#         return self.user.username + "'s" + " " + self.meal.mymeal.type