from django.db import models

# Create your models here.
from django.db import models

class Persona(models.Model):
    choices_genero = [('h', 'Hombre'), ('m', 'Mujer')]
    nombres = models.CharField(verbose_name="nombres", max_length=50)
    apellidos = models.CharField(verbose_name="apellidos", max_length=50)
    genero = models.CharField(verbose_name="genero", max_length=1, choices=choices_genero)
    documento_identificacion = models.CharField(verbose_name="cedula", max_length=50)
    email = models.CharField(verbose_name="email", max_length=50)
    telefono = models.CharField(verbose_name="telefono", max_length=50)
    fechaNacimiento = models.DateField(verbose_name="fecha Nacimiento")
    direccion = models.CharField(verbose_name="direccion", max_length=150)

    def __str__(self):
        return self.nombres

class Rol(models.Model):
    choices_rol = [('administrador', 'Administrador'), ('cliente', 'Cliente')]
    nombre_rol = models.CharField(verbose_name="nombreRol", max_length=50, choices=choices_rol)

    def __str__(self):
        return self.nombre_rol

class Usuario(Persona):
    nombre_usuario = models.CharField(verbose_name="usuario", max_length=50)
    password = models.CharField(verbose_name="password", max_length=50)
    rol = models.ManyToManyField(Rol, related_name="usuarios")
       

class Cuenta(models.Model):
    usuarioCuenta = models.ManyToManyField(Usuario, related_name="cuentaUsuario")
    fechaCreacion = models.DateField(verbose_name="fecha Creacion")
    fechaActualizacion = models.DateField(verbose_name="fecha Actualizacion")
    imagen = models.ImageField(verbose_name="imagen")
    numero_horas = models.IntegerField(verbose_name="numeroHoras")

class Categoria(models.Model):
    nombre_categoria = models.CharField(verbose_name="nombre Categoria", max_length=100)
    nombre_logo = models.CharField(verbose_name="nombre Logo", max_length=100)
    descripcion = models.CharField(verbose_name= "descripcion", max_length= 200)
    choices_estado = [('habilitado', 'Habilitado'), ('Deshabilitado', 'Deshabilitado')]
    fecha_creacion = models.DateField(verbose_name="fecha Creacion")
    def __str__(self):
        return self.nombre_categoria

class Interes(models.Model):
    usuarioIntereses = models.ManyToManyField(Usuario, related_name="intereses")
    categoria = models.ManyToManyField(Categoria, related_name="categorias")

class Calificacion(models.Model):
    puntuacion = models.IntegerField(verbose_name="puntuacion")
    comentarios = models.CharField(verbose_name="password", max_length=50)
    usuario = models.ForeignKey(Usuario,related_name= "usuarios")

class Servicios(models.Model):
    titulo = models.CharField(verbose_name="Titulo", max_length=150)
    descripcion_actividad = models.CharField(verbose_name="descripcion",max_length=256)
    tiempo_requerido = models.IntegerField(verbose_name="numero de horas requerida")
    choices_rol = [('Oferta', 'Oferta'), ('Demanda', 'Demanda')]
    fecha_creacion =models.DateField(verbose_name="fecha_creacion")
    fecha_vigente =models.DateField(verbose_name="fecha_vigente")
    propietario=models.ManyToManyField(Usuario, related_name="propietario")
    choices_rol = [('Vigente', 'Vigente'), ('No vigente', 'No vigente')]    
    ofertante_Demandate=models.ManyToManyField(Usuario,related_name="ofertanteDemandante")

class Transaccion_Tiempo(models.Model):
    numero_horas = models.IntegerField(verbose_name="horas_Transferencia")
    numero_minutos= models.IntegerField(verbose_name="minutos")
    descripcion = models.CharField(verbose_name="descripcion",max_length=256)
    ofertante= models.ManyToManyField(Usuario, related_name="ofertante")
    demandante= models.ManyToManyField(Usuario, related_name="demandante")
    fechaTransaccion= models.DateField(verbose_name="fecha_transaccion")