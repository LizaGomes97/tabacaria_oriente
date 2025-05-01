from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from .models import Perfil

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(usuario=user)
            messages.success(request, 'Conta criada com sucesso! Você já pode fazer login.')
            return redirect('usuarios:login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'usuarios/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {username}!')
                # Redirecionar para a página que o usuário estava tentando acessar
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('produtos:lista_produtos')
        else:
            messages.error(request, 'Erro de autenticação. Por favor, verifique suas credenciais.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso!')
    return redirect('produtos:lista_produtos')

@login_required
def profile(request):
    try:
        perfil = request.user.perfil
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(usuario=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('usuarios:perfil')
    else:
        form = UserProfileForm(instance=perfil)
    
    return render(request, 'usuarios/perfil.html', {'form': form})