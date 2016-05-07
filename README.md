# cursoshop
Proyecto de carrito de compras Y LMS-little para la enseñanza de Tecnologias WEB a los estudiantes de Tecnologia en desarrollo de sistemas de información UPC 


# Pasos para crear crear un proyecto

* una vez se cuente con django instaldo en el equipo un proyecto se crear de la siguiente manera
	```
	django-admin startproject [cursoshop] 
	```
	Donde cursoshop es el nombre de este proyecto que quedará almacenado en el directorio donde ejecutemos el comando anterior. Este creara un subdirectorio con el mismo nombre del proyecto donde encontraremos un archivo llamado `settings.py` donde se encuentra la configuración general del proyecto (Zona horaria, Acceso a DB, ruta de templates, archivos estáticos, etc) y un archivo llamado `url.py` donde se configuraran las urls de acceso a nuestra aplicaciòn

* Para comenzar a trabajar con nuestro proyecto debemos hacerlo por lo menos en un app. Una app es un módulo que alberga el código de modelos, vistas, helpers, validators etc que están relacionados de alguna manera. En este caso crearemos una sola app que contendrá lo anteriormente mencionado. La llamaremos main (pero puede ser cualquier nombre lo ideal es que tenga un nombre de acuerdo a la función de la aplicación). Ingresamos a la carpeta de nuestro proyecto y ejecutamos:

	```
	python manage.py startapp [main]
	```
	En el archivo de `settings.py` se debemos agregar el nombre de nuestra app `main` a la tupla `INSTALLED_APPS`

	Listo! ya podemos iniciar a crear nuestros modelos y vistas.

# Usando el admin de django
El sitio administrativo de django es un backend que nos da la facilidad de crear toda una funcionalidad de operaciones CRUD. Pero no significa que con esto haremos todo nuestro proyecto, sencillamente aqui podrémos manipular algunas tablas de referencia de nuestra base de datos y dar acceso administrativo algunos usuarios que tengan permisos de INSERT, UPDATE o DELETE sobre las mismas. Mas no es una aplicación para usarse como FrontEnd. para poder usarlo necesitamos hacer lo siguiente:

* Verificar en nuestro archivo `settings.py` se encuentre la app `django.contrib.admin` en `INSTALLED_APPS`

* Tener nuestro modelo creado en `models.py` que se encuentra en el directorio de nuestra aplicacición. Para este caso registrare el modelo Curso

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

* En el archivo `admin.py` debemos registrar nuestro modelo para que el backend de administración lo pueda gestionar.

	```
	@admin.register(Course)
	class CourseAdmin(admin.ModelAdmin):
	    search_fields = ('name', 'price', 'teacher__name')
	    list_display = ('name', 'price', 'teacher')
	    
	```

	Más información del [admin](https://docs.djangoproject.com/es/1.9/ref/contrib/admin/)

* En el archivo de `urls.py` deben estar habilitadas las url para acceder al sitio de administración.

	```
	urlpatterns = [
	    url(r'^admin/', admin.site.urls),
	]
	```

* Ya podemos empezar a usar nuestro backend de administración. Si no contamos con un usuario en nuestra base de datos podemos crear uno mediante

	```
	python manage.py createsuperuser
	```

	o si desea cambiar el password

	```
	python manage.py changepassword [user]
	```

	donde user corresponde al nombre de usuario registrado.


# Extendiendo el modelo User de Django

Django provee modelos de usuarios , grupos, permisos y otros más para la autenticación, de manera que podamos reutilizarlo sin tener que reinventar la rueda. Pero el modelo `User` es muy limitado en atributos y si queremos adicionar más sin perder la funcionalidad que brinda la autenticación debemos realizar algunos ajustes a nuestros modelos. Por ejemplo, en este proyecto se requieren don modelos para el manejo de usuario (Profesor y Usuarios) cada uno necesita de unos datos base proporcionados por el User de Django ( `first_name`, `last_name`, `email`, `password`, `username`, `is_active`) pero surge la necesidad de que el profesor debamos almacenar su profesion y perfil; asi como para los usuario el sexo. 

Por ello, que debemos crear dos modelos ( `Teacher` y `Usuario`) omitiendo los atributos que ya posee el modelo `User` y agregando los que le pertenecen a cada uno. Adicionalmente para que exista un vinculo entre nuestros modelos y el proporcionado por Django realizaremos una relación 1:1 entre estos.

	```
	class Teacher(models.Model):
	    id = models.OneToOneField(User, primary_key = True)
	    job = models.CharField(max_length = 100)
	    profile = models.TextField()

	    def __unicode__(self):

	list_sexo = ( ('M', 'Masculino') , ('F', 'Femenino'))
	class Usuario(models.Model):
	    id = models.OneToOneField(User, primary_key = True)
	    sexo = models.CharField( max_length=1, choices = list_sexo)
	```

	Si verificamos el atributo id referencia al modelo de usuarios por lo que todos los atributos y metodos de User  se accederan a tráves del atributo id de las instancias de estas clases.


# Haciendo mi primera vista

* crear una vista en `views.py` que retorne una salida HTTP por ejemplo
	```
	def index(request):
	    """view principal
	    """
	   return render_to_response('index.html')
	```

	Si queremos enviar datos a nuestra vista

	```
	def index(request):
	    """view principal
	    """
	    cursos = Course.objects.all() # podemos cachear la consulta a la base de datos para enviarsela a la template con el nombre de cursos
	    return render_to_response('index.html',  {'cursos': cursos } )
	```

	Si queremos enviar informaciòn de la variable request (por ejemplo para informacion de usuario request.user)
	en este caso con `RequestContext(request)`

	```
	def index(request):
	    """view principal
	    """
	    cursos = Course.objects.all() # podemos cachear la consulta a la base de dat
	    return render_to_response('index.html',  {'cursos': cursos }, context_instance = RequestContext(request) )
	```

* Debemos crear el template `index.html` el cual renderiza esta view. en `settings.py` podemos verificar en la lista de `TEMPLATES` la ruta de estas dentro del proyecto.

* una vez tengamos nuestra vista debemos incluir la url para que sea accesible por nuestros usuarios.

	```
	 url('^$', index , name = 'index'), # el primer parametro es la expresiòn regular, el segundo la vista a la que llama y el tercero el nombre de la url que podra accederse deste el template

	```






