from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import ServicioSerializers,CuentaSerializers
from .models import Servicio,Cuenta

# Create your views here.
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializers

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializers

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializers