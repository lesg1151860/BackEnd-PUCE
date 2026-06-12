from django.contrib import admin
from .models import CasoSIUCE

@admin.register(CasoSIUCE)
class CasoSIUCEAdmin(admin.ModelAdmin):
    # Campos que se calculan automáticamente en el save()
    readonly_fields = ('avance_ie', 'avance_sem', 'avance_general', 'estado', 'fecha_registro')
    
    # Visualización en la tabla de lista
    list_display = ('radicado_sac', 'estado', 'avance_general', 'fecha_registro')
    
    # Filtros para facilitar la gestión
    list_filter = ('estado', 'fecha_registro')
    
    # Buscador por radicado o víctima
    search_fields = ('radicado_sac', 'estudiante_victima')