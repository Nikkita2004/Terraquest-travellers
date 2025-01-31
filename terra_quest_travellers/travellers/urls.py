from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # Add this line
    path('services/', views.services, name='services'),
    path('packages/', views.packages, name='packages'),
    path('gallery/', views.gallery, name='gallery'),
    path('blogs/', views.blogs, name='blogs'),
    path('reviews/', views.reviews, name='reviews'),
    path('book/', views.book, name='book'),
]