from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.


class Chapter(models.Model):
    name = models.CharField(max_length= 120)

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length = 120)
    page = HTMLField()
    chapter = models.ForeignKey(Chapter)

    def __unicode__(self):
        return self.title

class Teacher(models.Model):
    name = models.CharField(max_length= 120)
    job = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length= 120)
    price = models.FloatField()
    teacher = models.ForeignKey(Teacher)
    Chapter = models.ManyToManyField(Chapter)
    image = models.ImageField(upload_to = 'static/uploads/')

    def __unicode__(self):
        return self.name

class Usuario(User):
    class Meta:
        proxy = True
