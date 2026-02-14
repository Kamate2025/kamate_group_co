from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TechServiceRequestForm, TechCourseEnrollmentForm
from django.views.generic import ListView
from .models import TechCourse


def tech_home(request):
    return render(request, 'tech/tech_home.html')


def tech_service_request(request):
    if request.method == 'POST':
        form = TechServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Form submitted successfully - one of our agents will reach out to you shortly strictly via +256 787 360 381 to discuss further on your system requirements."
            )
            return redirect('tech_service_request')
    else:
        form = TechServiceRequestForm()

    return render(request, 'tech/tech_service_request.html', {'form': form})


class TechCourseListView(ListView):
    model = TechCourse
    template_name = 'tech/tech_classes.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return TechCourse.objects.filter(availability=True)


def tech_class_enroll(request, slug):
    course = get_object_or_404(TechCourse, slug=slug, availability=True)

    if request.method == "POST":
        form = TechCourseEnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()

            messages.success(
                request,
                "Form Submitted successfully. Admin will contact you through +256 787 360 381 to discuss further details. We reply within minutes during business days."
            )

            form = TechCourseEnrollmentForm()

    else:
        form = TechCourseEnrollmentForm()

    context = {
        "course": course,
        "form": form,
    }

    return render(request, "tech/tech_class_enroll.html", context)
