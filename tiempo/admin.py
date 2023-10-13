from django.contrib import admin
from .models import Rol,Usuario,Cuenta,Categoria,Interes,Calificacion,Servicios,Transaccion_Tiempo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(Interes)
admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(Calificacion)
admin.site.register(Servicios)
admin.site.register(Transaccion_Tiempo)
