# description_generator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_description/', views.generate_description, name='generate_description'),
]
