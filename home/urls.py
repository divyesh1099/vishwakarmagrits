from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.my_login, name = 'login'),
    path('logout', views.my_logout, name = 'logout'),
    path('signup', views.my_signup, name = 'signup'),
    path('view_profile', views.view_profile, name = 'view_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('delete_profile', views.delete_profile, name='delete_profile'),
    path('meal/<str:type>', views.meal, name='meal'),
    path('item/<str:name>', views.item, name='item'),
]