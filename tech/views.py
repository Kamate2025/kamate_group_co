from django.shortcuts import render

def tech_home(request):
    return render(request, 'tech/tech_home.html')
