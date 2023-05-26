from django.urls import path
from . import views


# Validacion de usuario en login 
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]