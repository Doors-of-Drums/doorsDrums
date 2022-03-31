from django.contrib import admin
from .models import Usuario, Cancion

# Register your models here.

# modelo de Usuario
admin.site.register(Usuario)

# modelo de Cancion
admin.site.register(Cancion)
