from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
    """view principal
    """
    return render_to_response('index.html')

def login(request):
    """view del login
    """
    return render_to_response('login.html')

def search(request):
    """view de los resultados de busqueda
    """
    return render_to_response('login.html')

def about(request):
    """view del acerca de ...
    """
    return render_to_response('acerca.html')

def me(request):
    """view del profile
    """
    return render_to_response('perfil.html')

def contacto(request):
    """view del profile
    """
    return render_to_response('contactanos.html')


def registro(request):
    """view del profile
    """
    return render_to_response('registrarse.html')
