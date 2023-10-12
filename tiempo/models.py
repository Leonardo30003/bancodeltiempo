from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombreCategorias = models.CharField(max_length=100)

class Persona(models.Model):
    choices_genero = [('h','Hombre'),('M','Mujer')]
    nombres = models.CharField(verbose_name = "nombres", max_length=50)
    apellidos = models.CharField(verbose_name ="apellidos", max_length=50)
    genero = models.CharField(verbose_name ="genero", max_length=50, choices = choices_genero)
    documento_identificacion = models.CharField(verbose_name ="cedula", max_length=50)
    email = models.CharField(verbose_name ="email", max_length=50)
    telefono = models.CharField(verbose_name ="telefono", max_length=50)
    fechaNacimiento = models.DateField(verbose_name="fecha Nacimiento")
    direccion = models.CharField(verbose_name="direccion",max_length=150)
    
    def _str_(self):
        return self.nombres 