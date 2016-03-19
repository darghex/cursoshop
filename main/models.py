from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Chapter(models.Model):
    name = models.CharField(max_length= 120)


class Topic(models.Model):
    title = models.CharField(max_length = 120)
    page = HTMLField()
    chapter = models.ForeignKey(Chapter)

class Teacher(models.Model):
    name = models.CharField(max_length= 120)
    job = models.CharField(max_length = 100)

class Course(models.Model):
    name = models.CharField(max_length= 120)
    price = models.FloatField()
    teacher = models.ForeignKey(Teacher)
    Chapter = models.ManyToManyField(Chapter)
    image = models.ImageField(upload_to = 'uploads/')
