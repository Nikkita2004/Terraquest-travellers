from django.shortcuts import render

def home(request):
    return render(request, 'travellers/home.html')

from django.shortcuts import render

def about(request):
    return render(request, 'travellers/about.html')  # Ensure the template exists
    
from django.shortcuts import render

def services(request):
    return render(request, 'travellers/services.html')  # Ensure the template exists

from django.shortcuts import render

def packages(request):
    return render(request, 'travellers/packages.html')

from django.shortcuts import render

def gallery(request):
    return render(request, 'travellers/gallery.html')

from django.shortcuts import render

def blogs(request):
    return render(request, 'travellers/blogs.html')

from django.shortcuts import render

def reviews(request):
    return render(request, 'travellers/reviews.html')

from django.shortcuts import render

def book(request):
    return render(request, 'travellers/book.html')