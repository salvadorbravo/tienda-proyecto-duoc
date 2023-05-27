from django.shortcuts import render, redirect
from django.views import View
from .models import Cliente, Producto, Carrito, PedidoRealizado
from .forms import FormularioRegistroUsuario, FormularioPerfilCliente
from django.contrib import messages
from django.http import JsonResponse
# from django.contrib.auth import authenticate, login, logout


# Validación de usuario en Login
# def login_view(request):
#     if request.method == 'Validate':
#         username = request.Validate['username']
#         password = request.Validate['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('')  # Entre '' debe ir la dirección de login
#         else:
#             messages.error(request, 'Usuario o contraseña incorrectos.')
    
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login')  

# Vista del home
def inicio(request):
    return render(request, 'core/inicio.html')

# Vista del Registro de Usuario
class VistaRegistroCliente(View):
    def get(self, request):
        formulario = FormularioRegistroUsuario()
        return render(request, 'core/test-registro.html', {'formulario':formulario})
    
    def post(self, request):
        formulario = FormularioRegistroUsuario(request.POST)
        if formulario.is_valid():
            messages.success(request, 'Registrado Correctamente')
            formulario.save()
        return render(request, 'core/test-registro.html', {'formulario':formulario})
    
# Vista del Perfil
class VistaPerfil(View):
    def get(self, request):
        form = FormularioPerfilCliente()
        return render(request, 'core/perfil.html', {'form':form,
        'active':'btn-primary'})
        
    def post(self, request):
        form = FormularioPerfilCliente(request.POST)
        if form.is_valid():
            usr = request.user
            nombre = form.cleaned_data['nombre']
            localidad = form.cleaned_data['localidad']
            ciudad = form.cleaned_data['ciudad']
            region = form.cleaned_data['region']
            codigo_postal = form.cleaned_data['codigo_postal']
            reg = Cliente(user=usr, nombre=nombre, localidad=localidad, ciudad=ciudad, region=region, codigo_postal=codigo_postal)
            reg.save()
            messages.success(request, 'Perfil Actualizado')
        return render(request, 'core/perfil.html', {'form':form,
        'active':'btn-primary'})