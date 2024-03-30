from Credentialsapp.forms import UserRegistrationForm, DealerRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def main_home(request):
    return render(request, 'main_home.html')

def user_home(request):
    return render(request, 'user_home.html')

def dealer_home(request):
    return render(request, 'dealer_home.html')

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_home')  
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

def dealer_registration(request):
    if request.method == 'POST':
        form = DealerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('dealer_home')  
    else:
        form = DealerRegistrationForm()
    return render(request, 'dealer_registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'USER':
                    return redirect('user_home')
                elif user.role == 'DEALER':
                    return redirect('dealer_home')
            else:
                print("Authentication failed.")
        else:
            print("Form is invalid:", form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})