"""cursoshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from main.views import *
from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', index , name = 'index'),
    url('^login$', login, name = 'login' ), #/login
    url('^logout$', logout, name = 'logout' ), #/login
    url('^home$', home, name = 'home' ), #/home
    url('^profile$', home, name = 'profile' ), #/profile
    url('^about$', about, name = 'about' ),
    url('^me$', me, name = 'me' ),
    url('^search$', search, name = 'search' ),
    url('^register$', registro, name = 'register' ),
    url('^contacts$', contacto, name = 'contacts' ),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
]
