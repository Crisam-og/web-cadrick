from django.db import models
import uuid
from django.conf import settings
from datetime import datetime

# Create your models here.
# class Nosotros(models.Model):
#     id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
#     historia = models.TextField()
#     mision = models.TextField()
#     vision = models.TextField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated = models.DateTimeField(auto_now = True)
    
#     def __str__(self):
#         return self.id
#     def toJSON(self):
#         item = {'id': self.id, 
#                 'historia': self.historia, 
#                 'mision': self.mision, 
#                 'vision': self.vision
#                 }
#         return item
# class Configuraciones(models.Model):
#     id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
#     nombre_config = models.CharField(max_length=100, verbose_name="Nombre de la Configuracion")
#     valor = models.CharField(max_length=255, verbose_name="Valor de la Configuración")
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated = models.DateTimeField(auto_now = True)
#     def __str__(self):
#         return self.nombre_config 
class Galeria(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False) 
    titulo_principal = models.CharField(max_length=100, verbose_name="Titulo principal", blank=True)
    nombre_boton = models.CharField(max_length=100, verbose_name="Nombre boton", blank=True, default="#")
    url_boton = models.URLField(max_length=200, verbose_name="Enlace boton")
    sub_section_proyectos = models.TextField(verbose_name="Subtitulo Seccion Proyectos", blank=True)
    sub_section_servicios = models.TextField(verbose_name="Subtitulo Seccion Servicios", blank=True)
    sub_section_clientes = models.TextField(verbose_name="Subtitulo Seccion Clientes", blank=True)
    sub_section_cursos = models.TextField(verbose_name="Subtitulo Seccion Cursos", blank=True)
    imagen_principal_1 = models.ImageField(upload_to='system/images/galeria/', verbose_name="Imagen Portada Principal 1")
    imagen_principal_2 = models.ImageField(upload_to='system/images/galeria/', verbose_name="Imagen Portada Principal 2")
    imagen_principal_3 = models.ImageField(upload_to='system/images/galeria/', verbose_name="Imagen Portada Principal 3")
    imagen_mision = models.ImageField(upload_to='system/images/galeria/', verbose_name="Imagen Misión")
    imagen_vision = models.ImageField(upload_to='system/images/galeria/', verbose_name="Imagen Visión")

    def get_image(self, image_field='imagen'):
        image = getattr(self, image_field)
        if image:
            return '{}{}'.format(settings.MEDIA_URL, image)
        return '{}{}'.format(settings.STATIC_URL, 'img/image_not_found.png')
    
class Compania(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_compania = models.CharField(max_length=100, verbose_name="Nombre de la compañia")
    email = models.EmailField(max_length=100, verbose_name="Email")
    telefono = models.CharField(max_length=9, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    url_whatsapp = models.CharField(max_length=255, verbose_name="Url Whatsapp")
    historia = models.TextField(verbose_name="Acerca de")
    mision = models.TextField(verbose_name="Misión")
    vision = models.TextField(verbose_name="Visión")
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.nombre_compania
        
class Equipo(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_equipo = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    apellido_equipo = models.CharField(max_length=100, unique=True, verbose_name="Apellido")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='system/images/equipo/', verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nombre_equipo
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(settings.MEDIA_URL, self.imagen)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')

class TipoServicio(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_tipo_servicio = models.CharField(max_length=100, unique=True, verbose_name="Nombre del tipo de servicio")
    def __str__(self):
        return self.nombre_tipo_servicio

class Servicios(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_servicio = models.CharField(max_length=100, unique=True, verbose_name="Nombre del servicio")
    descripcion_servicio = models.TextField(verbose_name="Descripción")
    servicio_id = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name="Seleciones un tipo de servicio")
    imagen = models.ImageField(upload_to='system/images/servicios/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    estado = models.BooleanField(default=True, verbose_name="Estado")
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nombre_servicio
    
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(settings.MEDIA_URL, self.imagen)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')
            
    def toJSON(self):
        item = {'id': self.id, 
                'nombre_servicio': self.nombre_servicio, 
                'description': self.descripcion_servicio, 
                'imagen': self.imagen.url
                }
        return item
    
class Proyectos(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_proyecto = models.CharField(max_length=100, unique=True, verbose_name="Titulo")
    descripcion_corta = models.TextField(verbose_name="Descripción Corta", max_length=240)
    descripcion_detallada = models.TextField(verbose_name="Descripción Detallada")
    fecha_de_proyecto = models.DateField(default=datetime.now, verbose_name="Fecha del Proyecto")
    cliente = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Cliente")
    imagen = models.ImageField(upload_to='system/images/proyectos/', verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nombre_proyecto
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(settings.MEDIA_URL, self.imagen)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')

class Clientes(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_cliente = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    imagen = models.ImageField(upload_to='system/images/clientes/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nombre
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(settings.MEDIA_URL, self.imagen)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')
    

#Cursos
class Capacitador(models.Model):
    GRADO = [
        ('Bachiller', 'BACHILLER'),
        ('Magister', 'MAGISTER'),
        ('Doctor', 'DOCTOR'),
    ]
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_capacitador = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos_capacitador = models.CharField(max_length=100, verbose_name="Apellidos")
    profesion = models.CharField(max_length=255, verbose_name="Profesión")
    grado_academico = models.CharField(max_length=15, choices=GRADO, verbose_name='Grado Académico', null=True, blank=True) 
    descripcion_c = models.TextField(verbose_name="Descripción", null=True, blank=True)
    correo = models.EmailField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(upload_to='system/images/capacitadores/', null=True, blank=True, verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nombre_capacitador + ' ' +self.apellidos_capacitador
    
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(settings.MEDIA_URL, self.imagen)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')
    
    def toJSON(self):
        item = {'id': self.id, 
                'nombre_capacitador': self.nombre_capacitador, 
                'apellidos_capacitador': self.apellidos_capacitador, 
                'grado_academico': self.grado_academico, 
                'descripcion_c': self.descripcion_c,
                'correo': self.correo, 
                'imagen': self.imagen.url
                }
        return item

class Cursos(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_curso = models.CharField(max_length=255, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)
    fecha_de_inicio = models.DateField(default=datetime.now, verbose_name="Fecha de Inicio")
    horario = models.TextField(verbose_name="Horario", null=True, blank=True)
    duracion = models.TextField(verbose_name="Duración", null=True, blank=True)
    costo = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Costo")
    capacitador_id = models.ForeignKey(Capacitador, on_delete=models.CASCADE, verbose_name="Capacitador")
    temario = models.FileField(upload_to='system/documentos/temarios/', null=True, blank=True, verbose_name="Temario")
    imagen = models.ImageField(upload_to='system/images/cursos/', verbose_name="Imagen")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.nombre_curso
    
    def get_image(self):
        if self.imagen:
            return '{}{}'.format(settings.MEDIA_URL, self.imagen)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')
    def get_document(self):
        if self.temario:
            return '{}{}'.format(settings.MEDIA_URL, self.temario)
        return '{}{}'.format(settings.STATIC_URL, 'img/icon_doc_failed.png')

class Inscripciones(models.Model):
    GRADO = [
        ('Bachiller', 'BACHILLER'),
        ('Magister', 'MAGISTER'),
        ('Doctor', 'DOCTOR'),
    ]
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique=True, editable=False)
    nombre_ins = models.CharField(max_length=255, verbose_name="Nombre")
    apellidos_ins = models.CharField(max_length=100, verbose_name="Apellidos")
    telefono = models.CharField(max_length=9, verbose_name="Teléfono")
    correo = models.EmailField(max_length=255, verbose_name="Correo")
    profesion = models.CharField(max_length=255, verbose_name="Profesión", null=True, blank=True)
    grado_academico = models.CharField(max_length=15, choices=GRADO, verbose_name='Grado Académico', null=True, blank=True)
    curso_id = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name='Seleccione el curso de su interes')
    consulta = models.TextField(verbose_name="Consulta",max_length=150)
    created_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nombre_ins

