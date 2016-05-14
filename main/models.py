from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.


class Chapter(models.Model):
    name = models.CharField(max_length= 120)
    course  = models.ForeignKey('Course')

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length = 120)
    page = HTMLField()
    chapter = models.ForeignKey(Chapter)

    def __unicode__(self):
        return self.title


class Departamento(models.Model):
    nombre = models.CharField(max_length = 70)


class Ciudad(models.Model):
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length = 70)


class Teacher(models.Model):
    id = models.OneToOneField(User, primary_key = True)
    job = models.CharField(max_length = 100)
    ciudad = models.ForeignKey(Ciudad)
    profile = models.TextField()
    foto = models.ImageField( upload_to = 'photos/') # verifcar variable MEDIA en settings


    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length= 120)
    price = models.FloatField()
    teacher = models.ForeignKey(Teacher)
    image = models.ImageField(upload_to = 'static/uploads/')

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural ="Cursos"

    def __unicode__(self):
        return self.name

list_sexo = ( ('M', 'Masculino') , ('F', 'Femenino'))
class Usuario(models.Model):
    id = models.OneToOneField(User, primary_key = True)
    sexo = models.CharField( max_length=1, choices = list_sexo)
    ciudad = models.ForeignKey(Ciudad)
    foto = models.ImageField( upload_to = 'photos/') # verifcar variable MEDIA en settings
