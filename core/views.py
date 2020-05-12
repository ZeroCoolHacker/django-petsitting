from django.shortcuts import render
from .models import Veterinarian


# Create your views here.
def home(request):
    return render(request, 'pages/home.html', {})


def contact(request):
    return render(request, 'pages/contact.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


def services(request):
    return render(request, 'pages/services.html', {})


def veterinarians(request):
    veterinarians = Veterinarian.objects.all()
    return render(request, 'pages/veterinarians.html', {'veterinarians': veterinarians})
