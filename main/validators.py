# -*- encoding: utf-8 -*-
class Validator():
    _post  = None
    required = []
    _message = ''

    def __init__(self, post):
        """
        Carga los datos provenientes de un formulario atraves de POST
        @param post: Datos que proviene de POST
        """
        self._post = post

    def is_empty(self, field):
        """
        Verifica si un campo de formulario es vacio
        @param field: nombre del campo de formulario
        """
        if field == '' or field is None:
            return True
        return False

    def is_valid(self):
        """
        Indica si existen errores de formuarlio
        @return Boolean
        """
        # validar campos vacios
        for field in self.required:
            if self.is_empty(self._post[field]):

                self._message = 'El campo %s no puede ser vacio' %  field
                return False
        #validar que las contraseñas sehan iguales
        if not self._post['password1'] == self._post['password2']:
            self._message = 'Las contraseñas no  coinciden'
            return False

    def getMessage(self):
        return self._message
