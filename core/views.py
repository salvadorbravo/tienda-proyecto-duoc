from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Validación de usuario en Login
def login_view(request):
    if request.method == 'Validate':
        username = request.Validate['username']
        password = request.Validate['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')  # Entre '' debe ir la dirección de login
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  
