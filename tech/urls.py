from django.urls import path
from . import views


urlpatterns = [
    path('', views.tech_home, name='tech_home'),
]
