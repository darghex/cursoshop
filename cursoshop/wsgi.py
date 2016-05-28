#!/usr/bin/python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cursoshop.settings")
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())





# Para modo desarrollo
""""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cursoshop.settings")

application = get_wsgi_application()"""
