from django.contrib import admin

from .models import *

# Register your models here.
class ItemInline(admin.StackedInline):
    model = Item

class MealAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]

admin.site.register(Meal, MealAdmin)