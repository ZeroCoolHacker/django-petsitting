from django.contrib import admin
from django.urls import path

from .views import (
    home,
    contact,
    about,
    services,
    veterinarians
)


app_name = 'core'


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('veterinarians/', veterinarians, name='veterinarians'),
]