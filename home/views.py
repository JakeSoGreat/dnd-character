from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CharacterForm, QuickSpellForm, QuickItemForm
from .models import Character


# Create your views here.
def home_page_view(request):
    return render(request, 'home.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
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
            from django.contrib.auth import login
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('home')
    return render(request, 'register.html')


def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def character_list(request):
    characters = Character.objects.filter(user=request.user)
    return render(request, 'character_list.html', {'characters': characters})


@login_required
def character_create(request):
    if request.method == 'POST':
        character_form = CharacterForm(request.POST)
        if character_form.is_valid():
            character = character_form.save(commit=False)
            character.user = request.user
            character.save()
            character_form.save_m2m()
            messages.success(request, 'Character saved successfully!')
            return redirect('character_detail', pk=character.pk)
    else:
        character_form = CharacterForm()
    return render(request, 'character_form.html', {
        'character_form': character_form,
    })


@login_required
def character_update(request, pk):
    character = get_object_or_404(Character, pk=pk, user=request.user)
    if request.method == 'POST':
        if 'add_spell' in request.POST:
            spell_form = QuickSpellForm(request.POST)
            if spell_form.is_valid():
                spell_form.save()
                messages.success(request, 'Spell added successfully!')
                return redirect('character_update', pk=pk)
        elif 'add_item' in request.POST:
            item_form = QuickItemForm(request.POST)
            if item_form.is_valid():
                item_form.save()
                messages.success(request, 'Item added successfully!')
                return redirect('character_update', pk=pk)
        else:
            character_form = CharacterForm(request.POST, instance=character)
            if character_form.is_valid():
                character = character_form.save(commit=False)
                character.save()
                character_form.save_m2m()
                messages.success(request, 'Character updated successfully!')
                return redirect('character_detail', pk=character.pk)
    else:
        character_form = CharacterForm(instance=character)
    spell_form = QuickSpellForm()
    item_form = QuickItemForm()
    return render(request, 'character_form.html', {
        'character_form': character_form,
        'spell_form': spell_form,
        'item_form': item_form
    })


@login_required
def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk, user=request.user)
    if request.method == 'POST':
        character.delete()
        messages.success(request, 'Character deleted successfully!')
        return redirect('character_list')
    return render(request, 'character_confirm_delete.html', {'character': character})


@login_required
def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk, user=request.user)
    return render(request, 'character_detail.html', {'character': character})
