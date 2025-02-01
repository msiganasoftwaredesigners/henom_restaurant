from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_list, name='happenings'),
    path('event/<slug:slug>/', views.events_detail, name='happening_detail'),
]
