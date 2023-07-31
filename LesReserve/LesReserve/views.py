from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def vista_principal(request):
    # Lógica de la vista principal
    return render(request, 'principal.html')

def vista_login(request):
    # Lógica de la vista principal
    return render(request, 'login.html')

def vista_reservas(request):
    # Lógica de la vista principal
    return render(request, 'login.html')

def vista_sucursales(request):
    # Lógica de la vista principal
    return render(request, 'sucursales.html')

def vista_recursos(request):
    # Lógica de la vista principal
    return render(request, 'recursos.html')

def vista_inicio(request):
    # Lógica de la vista principal
    return render(request, 'inicio.html')

def vista_config(request):
    # Lógica de la vista principal
    return render(request, 'config.html')

def vista_loginAlt(request):
    # Lógica de la vista principal
    return render(request, 'loginAlt.html')