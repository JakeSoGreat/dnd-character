from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import CharacterForm
from .models import Character

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

@login_required
def character_list(request):
    characters = Character.objects.filter(user=request.user)
    return render(request, 'character_list.html', {'characters': characters})

@login_required
def character_create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            return redirect('character_list')
    else:
        form = CharacterForm()
    return render(request, 'character_form.html', {'form': form})

@login_required
def character_update(request, pk):
    character = get_object_or_404(Character, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm(instance=character)
    return render(request, 'character_form.html', {'form': form})

@login_required
def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk, user=request.user)
    if request.method == 'POST':
        character.delete()
        return redirect('character_list')
    return render(request, 'character_confirm_delete.html', {'character': character})
