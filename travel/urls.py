from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.travel_home, name='travel_home'),
    path('travel_request/', views.travel_request, name='travel_request'),
]
