from django.db import models
from django.utils.text import slugify


class TechServiceRequest(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.phone}"

class TechCourse(models.Model):

    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    MODE_CHOICES = (
        ('online', 'Online'),
        ('physical', 'Physical'),
        ('hybrid', 'Hybrid'),
    )

    course_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField()
    image = models.ImageField(upload_to='tech_courses/')

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='online')

    duration = models.CharField(max_length=100, help_text="e.g. 6 Weeks")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    availability = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.course_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.course_name


class TechCourseEnrollment(models.Model):
    course = models.ForeignKey(TechCourse, on_delete=models.CASCADE, related_name="enrollments")
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.course.course_name}"
    
