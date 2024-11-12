# accounts/views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect('home')  # Redirect to the homepage
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
