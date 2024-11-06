
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),          # Homepage
    path('about/', views.about, name='about'),           # About page
    path('contact/', views.contact, name='contact'),     # Contact page
]
