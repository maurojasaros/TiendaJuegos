from django.contrib import admin
from .models import Juego, Categoria, PerfilUsuario

# Registro de modelos en el panel de administración de Django
admin.site.register(Juego)
admin.site.register(Categoria)
admin.site.register(PerfilUsuario)
