from django.db import models


class ContactInquiry(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Contact Inquiries'

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"
    
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TravelRequest(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    # Flight specific fields
    departure_airport = models.CharField(max_length=150, blank=True, null=True)
    destination = models.CharField(max_length=150, blank=True, null=True)
    travel_date = models.DateField(blank=True, null=True)

    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.service.name}"
