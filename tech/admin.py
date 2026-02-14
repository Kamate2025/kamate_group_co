from django.contrib import admin
from .models import TechServiceRequest, TechCourse, TechCourseEnrollment


@admin.register(TechServiceRequest)
class TechServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'phone')


@admin.register(TechCourse)
class TechCourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'price', 'availability')
    list_filter = ('availability',)
    search_fields = ('course_name',)
    prepopulated_fields = {"slug": ("course_name",)}
    ordering = ('course_name',)


@admin.register(TechCourseEnrollment)
class TechCourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'course',
        'phone',
        'email',
        'created_at'
    )
    list_filter = (
        'course',
        'created_at'
    )
    search_fields = (
        'full_name',
        'email',
        'phone',
        'course__course_name'
    )
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
