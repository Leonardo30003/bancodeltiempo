from rest_framework import serializers
from .models import Persona,Rol,Cuenta,Categoria,Interes,Calificacion,Servicio,TransaccionTiempo


class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'
        
class CuentaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class RolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        
class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class InteresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Interes
        fields = '__all__'
        
class CalificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

class TransaccionSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransaccionTiempo
        fields = '__all__'