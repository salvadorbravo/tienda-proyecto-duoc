from django.urls import path
from core import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .forms import FormularioLoginUsuario

# Validacion de usuario en login 
urlpatterns = [
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('', views.inicio),
    path('perfil/', views.VistaPerfil.as_view(), name='perfil'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/test-login.html', authentication_form=FormularioLoginUsuario), name='login'),
    path('registro/', views.VistaRegistroCliente.as_view(), name="registrocliente"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)