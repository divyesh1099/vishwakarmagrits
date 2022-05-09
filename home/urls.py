from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('meal/<str:type>', views.meal, name='meal'),
    path('item/<str:name>', views.item, name='item'),
]