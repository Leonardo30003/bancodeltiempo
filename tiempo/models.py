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
    nombre_usuario = models.CharField(verbose_name="Usuario", max_length=50)
    password = models.CharField(verbose_name="Contraseña", max_length=50)
    rol = models.ManyToManyField(Rol, related_name="usuarios", blank=True)

class Cuenta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cuentas", null=True, blank=True)
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(verbose_name="Fecha de Actualización")
    imagen = models.ImageField(verbose_name="Imagen")
    numero_horas = models.IntegerField(verbose_name="Número de Horas")

class Categoria(models.Model):
    nombre_categoria = models.CharField(verbose_name="Nombre de Categoría", max_length=100)
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    ESTADO_CHOICES = [('habilitado', 'Habilitado'), ('deshabilitado', 'Deshabilitado')]
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")

    def __str__(self):
        return self.nombre_categoria

class Interes(models.Model):
    usuario = models.ManyToManyField(Usuario, related_name="intereses", blank=True)
    categoria = models.ManyToManyField(Categoria, related_name="categorias", blank=True)

class Calificacion(models.Model):
    puntuacion = models.IntegerField(verbose_name="Puntuación")
    comentarios = models.CharField(verbose_name="Comentarios", max_length=50)
    usuario_calificacion = models.ManyToManyField(Usuario, related_name="calificaciones", blank=True)

class Servicio(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=150)
    descripcion_actividad = models.CharField(verbose_name="Descripción", max_length=256)
    tiempo_requerido = models.IntegerField(verbose_name="Horas Requeridas")
    ROL_CHOICES = [('Oferta', 'Oferta'), ('Demanda', 'Demanda')]
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")
    fecha_vigente = models.DateField(verbose_name="Fecha Vigente")
    propietario = models.ManyToManyField(Usuario, related_name="servicios_propietario", blank=True)
    estado = models.CharField(verbose_name="Estado", max_length=10, choices=[('Vigente', 'Vigente'), ('No vigente', 'No vigente')])
    ofertante_demandante = models.ManyToManyField(Usuario, related_name="servicios_ofertante_demandante", blank=True)

class TransaccionTiempo(models.Model):
    numero_horas = models.IntegerField(verbose_name="Horas de Transferencia")
    numero_minutos = models.IntegerField(verbose_name="Minutos")
    descripcion = models.CharField(verbose_name="Descripción", max_length=256)
    demandante = models.ManyToManyField(Usuario, related_name="transacciones_demandante", blank=True)
    fecha_transaccion = models.DateField(verbose_name="Fecha de Transacción")