from django.urls import path
# from .views import * tambien era valido pero para algo mas controlado
from . import views

urlpatterns = [
    path("", views.inicio),
    path("mensajito", views.mensajito),
    path("login/", views.login),
    path("configuracion", views.panel_admistrador_anuncios),
    path("configuracion/crear_anuncio", views.panel_cargar_anuncio),
]