from django.contrib import admin
from .models import (
    CasoSIUCE, TipoAgresion, TipoDano, 
    EventoGenerador, ClasificacionLey1620, 
    CatalogoAccionIE, CatalogoAccionSEM
)

# Registramos los catálogos y el caso principal
admin.site.register(TipoAgresion)
admin.site.register(TipoDano)
admin.site.register(EventoGenerador)
admin.site.register(ClasificacionLey1620)
admin.site.register(CatalogoAccionIE)
admin.site.register(CatalogoAccionSEM)

@admin.register(CasoSIUCE)
class CasoSIUCEAdmin(admin.ModelAdmin):
    # Esto te permite ver los campos calculados aunque no sean editables
    readonly_fields = ('avance_general', 'estado', 'fecha_registro')
    list_display = ('radicado_sac', 'estado', 'avance_general', 'fecha_registro')