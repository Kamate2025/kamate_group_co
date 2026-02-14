from django.contrib import admin
from .models import ContactInquiry, Service, TravelRequest


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")


@admin.register(TravelRequest)
class TravelRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "service", "phone", "created_at")
    list_filter = ("service", "created_at")
    search_fields = ("name", "phone", "email")
