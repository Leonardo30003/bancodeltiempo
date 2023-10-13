from django.contrib import admin
from .models import Rol,Usuario,Cuenta,Categoria,Interes

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(Interes)
admin.site.register(Rol)
admin.site.register(Categoria)
