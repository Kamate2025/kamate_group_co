from django.urls import path
from . import views


urlpatterns = [
    path('', views.tech_home, name='tech_home'),
    path('service_request/', views.tech_service_request, name='tech_service_request'),
    path('classes/', views.TechCourseListView.as_view(), name='tech_classes'),
    path('classes/<slug:slug>/enroll/', views.tech_class_enroll, name='tech_class_enroll'),
]

