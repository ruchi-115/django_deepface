# home/views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'home/homepage.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')
