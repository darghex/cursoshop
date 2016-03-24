# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from .models import Chapter
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.core.exceptions import NON_FIELD_ERRORS
# Create your views here.

def index(request):
    """view principal
    """
    return render_to_response('index.html' )

def login(request):
    """view del login
    """
    #Verificamos que los datos lleguen por el methodo POST
    formulario = LoginForm()
    if request.method == 'POST':
        #Cargamos el formulario (ver forms.py con los datos del POST)
        formulario = LoginForm(data = request.POST)
        #Verificamos que los datos esten correctos segun su estructura
        if formulario.is_valid():
            # Capturamos las variables que llegan por POST
            usuario = request.POST.get('usuario')
            clave = request.POST.get('clave')

            #validamos los datos de usuario y contraseña, el metodo authenticate verifica el password cifrado
            acceso = auth.authenticate(username = usuario, password = clave )
            #Si el usuario existe abrimos una sesion de usuario

            if not acceso is None:
                auth.login(request, acceso)
                return HttpResponseRedirect('/home')
            else:
                formulario._errors = { NON_FIELD_ERRORS:  'Usuario o Password Invalido'}


    return render_to_response('login.html', {"form": formulario} , context_instance = RequestContext(request))



def search(request):
    """view de los resultados de busqueda
    """
    return render_to_response('login.html')

@login_required(login_url="/login") # Protegemos la vista con el decorador del loguin para que solo pueda ingresar un usuario logueado
def home(request):
    """view de los resultados de busqueda
    """
    return render_to_response('perfil.html')


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

@login_required(login_url="/login") # Protegemos la vista con el decorador del loguin para que solo pueda ingresar un usuario logueado
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

def registro(request):
    """view del profile
    """
    return render_to_response('registrarse.html')
