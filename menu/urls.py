from django.urls import path
from .views import menu_view

from . import views

urlpatterns = [
    path('', views.menu_view, name='menus'),
    
]