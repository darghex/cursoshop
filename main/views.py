# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from .models import Chapter
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from .validators import FormRegistroValidator, FormLoginValidator

# Create your views here.

def index(request):
    """view principal
    """
    return render_to_response('index.html', context_instance = RequestContext(request) )

def login(request):
    """view del login
    """
    #Verificamos que los datos lleguen por el methodo POST

    if request.method == 'POST':
        #Cargamos el formulario (ver forms.py con los datos del POST)
        validator = FormLoginValidator(request.POST)
        #formulario = LoginForm(data = request.POST)
        #Verificamos que los datos esten correctos segun su estructura

        if validator.is_valid():
            # Capturamos las variables que llegan por POST
            usuario = request.POST['usuario']
            clave = request.POST['clave']
            auth.login(request, validator.acceso) # Crear una sesion
            return HttpResponseRedirect('/home')
        else:
            return render_to_response('login.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))

    return render_to_response('login.html', context_instance = RequestContext(request))


def search(request):
    """view de los resultados de busqueda
    """
    return render_to_response('login.html')

@login_required(login_url="/login")
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



from django.contrib.auth.hashers import make_password
from .models import Usuario
from validators import Validator
def registro(request):
    """view del profile
    """

    error = False
    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['nombre', 'apellidos', 'email','password1']

        if validator.is_valid():
            usuario = Usuario()
            #p = Persona.objects.get(documento = '123123123321')
            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellidos']
            usuario.username = request.POST['email']
            usuario.email = request.POST['email']
            usuario.password = make_password(request.POST['password1'])
            #TODO: ENviar correo electronico para confirmar cuenta
            usuario.is_active = True
            usuario.save()
            return render_to_response('registrarse.html', {'success': True  } , context_instance = RequestContext(request))
        else:
            return render_to_response('registrarse.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
    return render_to_response('registrarse.html', context_instance = RequestContext(request))
