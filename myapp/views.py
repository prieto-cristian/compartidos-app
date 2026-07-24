from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Pantalla de inicio: CARTELERA DE ANUNCIOS</h1")

def mensajito(request):
    return HttpResponse("<h1>Un paso mas cerca de ser Desarrollador Backend Python!</h1>")

def login(requets):
    return HttpResponse("<h1>Pantalla de login: REGISTRARSE / INICIAR SESION</h1>")

def panel_admistrador_anuncios(request):
    return HttpResponse("<h1>Panel administrador de anuncios</h1>")

def panel_cargar_anuncio(requets):
    return HttpResponse("<h1>Formulario para registrar un anuncio</h1>")