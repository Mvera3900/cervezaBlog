from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, "auth/registro.html", {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f"Bienvenido {username}!")
                return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, "auth/login.html", {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')