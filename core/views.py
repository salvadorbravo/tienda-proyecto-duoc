from django.shortcuts import render, redirect
from django.views import View
from .models import Cliente, Producto, Carrito, PedidoRealizado
from .forms import FormularioRegistroUsuario, FormularioPerfilCliente, FormularioContacto
from django.contrib import messages
from django.http import JsonResponse


# Vista de la lista de Productos (PRINCIPAL)
class VistaProducto(View):
    def get(self, request):
        audifonos = Producto.objects.filter(categoria='A')
        laptop = Producto.objects.filter(categoria='L')
        mobiles = Producto.objects.filter(categoria='M')
        teclados = Producto.objects.filter(categoria='T')
        return render(request, 'core/inicio.html', {'audifonos':audifonos, 'laptop':laptop, 'mobiles':mobiles, 'teclados':teclados})
    
# Vista del Detalle del Producto
class VistaDetalleProducto(View):
    def get(self, request, pk):
        producto = Producto.objects.get(pk=pk)
        return render(request, 'core/detalle-producto.html', {'producto':producto})
    
# Vista del Carrito de Compras
def añadir_carrito(request):
    user = request.user
    producto_id = request.GET.get('prod_id')
    producto = Producto.objects.get(id=producto_id)
    Carrito(user=user, producto=producto).save()
    return redirect('/carrito')

# Vista para Mostrar el Carrito de Compras
def mostrar_carrito(request):
    if request.user.is_authenticated:
        user = request.user
        carrito = Carrito.objects.filter(user=user)
        # Calculo matematico para lograr sumar la cantidad de productos en el carrito y sumando el costo de envio.
        pago = 0
        envio = 2000
        total_pago = 0
        productos_carrito = [p for p in Carrito.objects.all() if p.user == user]
        if productos_carrito:
            for p in productos_carrito:
               total_temporal = (p.cantidad * p.producto.precio_venta) 
               pago += total_temporal
               total_pago = pago + envio
            return render(request, 'core/añadir-carrito.html', {'carritos':carrito, 'total_pago':total_pago, 'pago':pago, 'envio':envio})
        else:
            return render(request, 'core/carrito-vacio.html')

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
            messages.success(request, 'DIRECCION REGISTRADA CORRECTAMENTE')
            form = FormularioPerfilCliente()  # Limpiar los campos del formulario
        return render(request, 'core/perfil.html', {'form':form,
        'active':'btn-primary'})
        
# Vista de los Audifonos
def audifono(request, data=None):
    if data == None:
        audifonos = Producto.objects.filter(categoria='A')
    return render(request, 'core/audifonos.html', {'audifonos':audifonos})

# Vista de los Laptop
def laptop(request, data=None):
    if data == None:
        laptops = Producto.objects.filter(categoria='L')
    return render(request, 'core/laptops.html', {'laptops':laptops})

# Vista del Telefono
def telefono(request, data=None):
    if data == None:
        telefonos = Producto.objects.filter(categoria='M')
    return render(request, 'core/telefono.html', {'telefonos':telefonos})

# Vista de los Teclados
def teclado(request, data=None):
    if data == None:
        teclados = Producto.objects.filter(categoria='T')
    return render(request, 'core/teclados.html', {'teclados':teclados})

# Vista de Formulario de Contacto
def contacto_vista (request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            messages.success(request, '¡Se ha enviado con exito!, nos comunicaremos con usted lo antes posible.')
            form.save()
            return render(request, 'contacto.html')
    else:
        form = FormularioContacto()
    return render(request, 'core/contacto.html', {'form': form})

# Vista del Contacto
def contacto(request):
    return render(request, 'core/contacto.html')

# Vista de las Direcciones
def direcciones(request):
    agregar = Cliente.objects.filter(user=request.user)
    return render(request, 'core/direcciones.html', {'agregar':agregar, 'active':'btn-primary'})

