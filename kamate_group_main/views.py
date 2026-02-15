from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
