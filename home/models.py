from email.policy import default
from django.db import models

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
        return self.type


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="items")
    image = models.ImageField(upload_to = "items/%Y/%m/%d/", default = "items/default.png")

    def __str__(self):
        return self.name