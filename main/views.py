from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate
from .models import Chapter
# Create your views here.

def index(request):
    """view principal
    """
    return render_to_response('index.html' )

def login(request):
    """view del login
    """
    user = request.POST.get('correo')
    clave = request.POST.get('clave')
    correcto = False
    usuario = authenticate(username = user, password = clave )
    if not usuario is None:
        correcto = True

    return render_to_response('login.html', {"correcto" : correcto  } , context_instance = RequestContext(request))

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
