from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
def teacher(request):
    return render(request, 'teacher.html') 
def result(request):
    return render(request, 'result.html')
def routine(request):
    return render(request, 'rutine.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def student(request):
    return render(request, 'student.html')
def contact(request):
    return render(request, 'contact.html')
def lab(request):
    return render(request, 'lab.html')
def club(request):
    return render(request, 'club.html')
def developer(request):
    return render(request, 'developer.html')
def login_page(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    else:
        return render(request, 'login.html')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')