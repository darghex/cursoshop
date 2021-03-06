# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from .models import Chapter,Course
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from .validators import FormRegistroValidator, FormLoginValidator
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib.auth.hashers import make_password
from .models import Usuario, Ciudad, Departamento
from validators import Validator
from cursoshop.settings import STATIC_ROLS

# Create your views here.

def index(request):
    """view principal
    """
    cursos = Course.objects.all()
    return render_to_response('index.html',  {'cursos': cursos }, context_instance = RequestContext(request) )

def login(request):
    """view del login
    """
    #Verificamos que los datos lleguen por el methodo POST

    if request.method == 'POST':
        #Cargamos el formulario (ver forms.py con los datos del POST)
        validator = FormLoginValidator(request.POST)
        #formulario = LoginForm(data = request.POST)
        #Verificamos que los datos esten correctos segun su estructurav
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
    cursos = None
    filter = None
    if 'filter' in request.GET.keys():
        filter = request.GET['filter']
        qset = ( Q( name__icontains = filter) |
                Q( price__icontains = filter) |
                Q( teacher__name__icontains = filter)
                )
        l_cursos = Course.objects.filter(qset)
        paginador = Paginator( l_cursos, 2)
        page = 1
        if 'page' in request.GET:
            page = request.GET['page']
        try:
            cursos = paginador.page(page)
        except EmptyPage:
            cursos = paginador.page( paginador.num_pages)
        except PageNotAnInteger:
            raise Http404("Pagina no encontrada")

        """
        Manera de realizar consultar por un criterio a la vez
        #buscamos por nombre del curso
        cursos = Course.objects.filter( name__icontains =  request.GET['filter'] )
        # Si no existen resultados buscarmos por precio
        if not cursos.exists():
            cursos = Course.objects.filter( price__icontains =  request.GET['filter'] )
        # Si no existen resultados buscarmos por profesor
        if not cursos.exists():
            cursos = Course.objects.filter( teacher__name__icontains =  request.GET['filter'] )
        filter = request.GET['filter']
        """


    return render_to_response('index.html', {'cursos': cursos, 'paginador': paginador, 'filtro': filter  }, context_instance = RequestContext(request))

@login_required(login_url="/login")
def home(request):
    """view de los resultados de busqueda
    """
    return render_to_response('index.html', context_instance = RequestContext(request))


def about(request):
    """view del acerca de ...
    """
    return render_to_response('acerca.html')

@login_required(login_url="/login")
def me(request):
    """view del profile
    """
    # si el metodo get no encuentra un objeto genera una excepcion DoesNotExist
    ciudades = Ciudad.objects.all()
    usuario = User.objects.get( id = request.user.id )
    save = False
    if request.method == 'POST':
        # Aqui realizar la respectiva validacion
        # Actulizar datos de usuario
        us = User.objects.get( id = request.user.id )
        us.first_name  = request.POST['first_name']
        us.last_name  = request.POST['last_name']
        us.email  = request.POST['email']
        us.save()
        save = True


    if request.user.groups.filter( id = STATIC_ROLS['TEACHER']).exists() :
        usuario_int = Teacher.objects.get( id__id = request.user.id )
    elif request.user.groups.filter( id = STATIC_ROLS['USER']).exists() :
        usuario_int = Usuario.objects.get( id__id = request.user.id )
    else:
        usuario_int = None

    if save and not usuario_int is None:
        usuario_int.ciudad_id = request.POST['ciudad']
        usuario_int.foto = request.FILES['newfoto']
        usuario_int.save()

    try:
        setattr(usuario, 'ciudad', usuario_int.ciudad )
        setattr(usuario, 'foto', usuario_int.foto )
    except:
        pass

    return render_to_response('perfil.html', { "usuario": usuario,  'ciudades': ciudades } , context_instance = RequestContext(request))


def contacto(request):
    """view del profile
    """
    return render_to_response('contactanos.html')

@login_required(login_url="/login") # Protegemos la vista con el decorador del loguin para que solo pueda ingresar un usuario logueado
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

from django.core import serializers
def ciudades(request):
    ciudades =  Ciudad.objects.filter(departamento_id = request.GET['departamento'])
    data = serializers.serialize('json', ciudades, fields=('id','nombre'))
    return HttpResponse( data , content_type ='application/json' )

from django.db import transaction
from django.core.mail import send_mail, EmailMultiAlternatives
from cursoshop.settings import EMAIL_HOST_USER

from django.template.loader import render_to_string

@transaction.atomic
def registro(request):
    """view del profile
    """

    error = False
    departamentos = Departamento.objects.all()
    ciudades =  Ciudad.objects.none()
    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['nombre', 'apellidos', 'email','password1', 'ciudad', 'departamento']

        if validator.is_valid():
            usuario = User()
            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellidos']
            usuario.username = request.POST['email']
            usuario.email = request.POST['email']
            usuario.password = make_password(request.POST['password1'])
            #TODO: ENviar correo electronico para confirmar cuenta
            usuario.is_active = True
            perfil = Group.objects.get(id = 3) # carga un perfil de tipo usuario
            usuario.save()
            usuario.groups.add( perfil )
            usuario.save()

            myusuario = Usuario()
            myusuario.id = usuario
            myusuario.sexo = request.POST['sexo']

            myusuario.ciudad_id = request.POST['ciudad']
            myusuario.save()
            #TODO: ENviar correo electronico para confirmar cuenta
            asunto = "Registro en cursoshop"
            body = render_to_string('email.html', { 'user': usuario})

            #send_mail(asunto, body, EMAIL_HOST_USER, [ usuario.email ] )
            msg = EmailMultiAlternatives(asunto, body, EMAIL_HOST_USER, [ usuario.email ] )
            msg.content_subtype = "html"
            msg.send()
            return render_to_response('registrarse.html', {'success': True  } , context_instance = RequestContext(request))
        else:
            return render_to_response('registrarse.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
    return render_to_response('registrarse.html', {'departamentos': departamentos, 'ciudades': ciudades }, context_instance = RequestContext(request))


@login_required(login_url='/login')
def notas(request):
    if request.user.groups.filter(id = 2).exists():
        return render_to_response('plantilla_notas.html', context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('/login')


def pdf(f):
    def funcion(*args, **kwargs):
        html = f(*args, **kwargs)
        result = StringIO() #creamos una instancia del un objeto StringIO para
        pdf = pisa.pisaDocument( html , result) # convertimos en pdf la template
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return funcion

import xhtml2pdf.pisa as pisa
from StringIO import StringIO
from django.template.loader import render_to_string
from cursoshop.settings import STATICFILES_DIRS


@pdf
def detalle_curso(request):
    curso = Course.objects.get( id = request.GET['curso'])
    return render_to_string("detalle_curso.html", { 'curso': curso, 'path': STATICFILES_DIRS[0] }) #obtenemos la plantilla
