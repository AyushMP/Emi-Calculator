from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate_emi/', views.calculate_emi, name='calculate_emi'),
]