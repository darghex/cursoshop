# cursoshop
Proyecto de carrito de compras Y LMS-little para la enseñanza de Tecnologias WEB a los estudiantes de Tecnologia en desarrollo de sistemas de información UPC 


# Pasos para crear crear un proyecto

1. una vez se cuente con django instaldo en el equipo un proyecto se crear de la siguiente manera
```
django-admin startproject [cursoshop] 
```
Donde cursoshop es el nombre de este proyecto que quedará almacenado en el directorio donde ejecutemos el comando anterior. Este creara un subdirectorio con el mismo nombre del proyecto donde encontraremos un archivo llamado `settings.py` donde se encuentra la configuración general del proyecto (Zona horaria, Acceso a DB, ruta de templates, archivos estáticos, etc) y un archivo llamado `url.py` donde se configuraran las urls de acceso a nuestra aplicaciòn

2. Para comenzar a trabajar con nuestro proyecto debemos hacerlo por lo menos en un app. Una app es un módulo que alberga el código de modelos, vistas, helpers, validators etc que están relacionados de alguna manera. En este caso crearemos una sola app que contendrá lo anteriormente mencionado. La llamaremos main (pero puede ser cualquier nombre lo ideal es que tenga un nombre de acuerdo a la función de la aplicación). Ingresamos a la carpeta de nuestro proyecto y ejecutamos:

```
python manage.py startapp [main]
```

Listo! ya podemos iniciar a crear nuestros modelos y vistas.

# Usando el admin de django
El sitio administrativo de django es un backend que nos da la facilidad de crear toda una funcionalidad de operaciones CRUD. Pero no significa que con esto haremos todo nuestro proyecto, sencillamente aqui podrémos manipular algunas tablas de referencia de nuestra base de datos y dar acceso administrativo algunos usuarios que tengan permisos de INSERT, UPDATE o DELETE sobre las mismas. Mas no es una aplicación para usarse como FrontEnd. para poder usarlo necesitamos hacer lo siguiente:

1. Verificar en nuestro archivo `settings.py` se encuentre la app `django.contrib.admin` en `INSTALLED_APPS`

2. Tener nuestro modelo creado en `models.py` que se encuentra en el directorio de nuestra aplicacición. Para este caso registrare el modelo Curso

```
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
```
Más información de [modelos](https://docs.djangoproject.com/es/1.9/ref/models/fields/)

3. En el archivo `admin.py` debemos registrar nuestro modelo para que el backend de administración lo pueda gestionar.

```
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price', 'teacher__name')
    list_display = ('name', 'price', 'teacher')
    
```

Más información del [admin](https://docs.djangoproject.com/es/1.9/ref/contrib/admin/)

4. En el archivo de `urls.py` deben estar habilitadas las url para acceder al sitio de administración.

```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```

5. Ya podemos empezar a usar nuestro backend de administración. Si no contamos con un usuario en nuestra base de datos podemos crear uno mediante

```
python manage.py createsuperuser
```

o si desea cambiar el password

```
python manage.py changepassword [user]
```

donde user corresponde al nombre de usuario registrado



