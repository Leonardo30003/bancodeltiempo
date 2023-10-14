from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Persona(AbstractUser):
    GENDER_CHOICES = [('h', 'Hombre'), ('m', 'Mujer')]
    first_name = models.CharField(verbose_name="Nombres", max_length=50)
    last_name = models.CharField(verbose_name="Apellidos", max_length=50)
    username=models.CharField(verbose_name="Username", max_length=100, unique=True)
    password=models.CharField(verbose_name="Password", max_length=100)
    genero = models.CharField(verbose_name="Género", max_length=1, choices=GENDER_CHOICES)
    documento_identificacion = models.CharField(verbose_name="Cédula", max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=50)
    telefono = models.CharField(verbose_name="Teléfono", max_length=50)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento",null=True, blank=True)
    direccion = models.CharField(verbose_name="Dirección", max_length=150,null=True, blank=True)

    def __str__(self):
        return self.first_name

class Rol(models.Model):
    ROLE_CHOICES = [('administrador', 'Administrador'), ('cliente', 'Cliente')]
    nombre_rol = models.CharField(verbose_name="Nombre de Rol", max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.nombre_rol

class Usuario(Persona):  
    rol = models.ManyToManyField(Rol, related_name="usuarios", null=True, blank=True)

class Cuenta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cuentas", null=True, blank=True)
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(verbose_name="Fecha de Actualización")
    imagen = models.ImageField(upload_to="fotos/",verbose_name="Imagen")
    numero_horas = models.IntegerField(verbose_name="Número de Horas")
  
class Categoria(models.Model):
    nombre_categoria = models.CharField(verbose_name="Nombre de Categoría", max_length=100)
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    ESTADO_CHOICES = [('habilitado', 'Habilitado'), ('deshabilitado', 'Deshabilitado')]
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")

    def __str__(self):
        return self.nombre_categoria

class Interes(models.Model):
    usuario = models.ManyToManyField(Usuario, related_name="intereses",null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, related_name="categorias",null=True, blank=True)

class Calificacion(models.Model):
    puntuacion = models.IntegerField(verbose_name="puntuacion")
    comentarios = models.CharField(verbose_name="password", max_length=50)
    usuario = models.ForeignKey(Usuario,related_name= "usuarios")
    
