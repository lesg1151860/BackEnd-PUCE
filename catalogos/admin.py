from django.contrib import admin
from .models import RolCiudadano, EstadoSAC, RespuestaSAC, ClasificacionCaso

# Registramos cada modelo una sola vez
admin.site.register(RolCiudadano)
admin.site.register(EstadoSAC)
admin.site.register(RespuestaSAC)
admin.site.register(ClasificacionCaso)