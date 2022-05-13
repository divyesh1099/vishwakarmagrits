from django.contrib import admin
from .models import *

# Register your models here.
class ItemInline(admin.StackedInline):
    model = Item

class MealAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]

# class UserMealInline(admin.StackedInline):
#     model = UserMeal

# class MyMealAdmin(admin.ModelAdmin):
#     inlines = [
#         UserMealInline,
#     ]

admin.site.register(Meal, MealAdmin)
# admin.site.register(MyMeal, MyMealAdmin)
admin.site.register(MyMeal)
admin.site.register(Profile)
