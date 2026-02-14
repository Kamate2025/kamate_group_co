from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactInquiryForm, TravelRequestForm


def travel_home(request):
    return render(request, 'travel/travel_home.html')


def contact_us(request):
    if request.method == "POST":
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message Submitted Successfully")
            return redirect("contact_us")
    else:
        form = ContactInquiryForm()

    return render(request, "contact_us.html", {"form": form})


def travel_request(request):
    if request.method == "POST":
        form = TravelRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Form submitted successfully. One of our team members will contact you strictly through +256 787 360 381."
            )
            return redirect("travel_request")
    else:
        form = TravelRequestForm()

    return render(request, "travel/request_form.html", {"form": form})
