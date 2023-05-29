from django.urls import path
from core import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .forms import FormularioLoginUsuario

# Validacion de usuario en login 
urlpatterns = [
    # path('', views.inicio),
    path('', views.VistaProducto.as_view(), name='inicio'),
    path('detalle-producto/', views.detalle_producto, name='detalle-producto'),
    path('perfil/', views.VistaPerfil.as_view(), name='perfil'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/test-login.html', authentication_form=FormularioLoginUsuario), name='login'),
    path('registro/', views.VistaRegistroCliente.as_view(), name="registrocliente"),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(next_page='login'), name='cerrar-sesion'), # Cierra la sesion y redirige a la pagina de login
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)