from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def home_page_view(request):  
    return HttpResponse("Hello, World!")

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'home' to your desired redirect
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(username=username, password=password)
            # Specify the backend explicitly
            from django.contrib.auth import login
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('home')
    return render(request, 'register.html')
