from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .models import UserProfile

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('u_name')
            password = form.cleaned_data.get('u_password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout(request):
    logout(request)
    return redirect('home')


def houses(request):
    return render(request, 'houses.html')

def prediction(request):
    return render(request, 'prediction.html')

def about_us(request):
    return render(request, 'about_us.html')

@login_required
def user_profile(request):
    return render(request, 'user_profile.html')
