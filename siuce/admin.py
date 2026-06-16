from django.contrib import admin
from .models import CasoSIUCE

@admin.register(CasoSIUCE)
class CasoSIUCEAdmin(admin.ModelAdmin):
    # Campos que se calculan automáticamente en el save()
    readonly_fields = ('porcentaje_avance_ie', 'porcentaje_avance_sem', 'avance_general', 'estado_siuce', 'fecha_registro')
    
    # Visualización en la tabla de lista
    list_display = ('num_radicado_siuce', 'estado_siuce', 'avance_general', 'fecha_registro')
    
    # Filtros para facilitar la gestión
    list_filter = ('estado_siuce', 'fecha_registro')
    
    # Buscador por radicado o víctima
    search_fields = ('num_radicado_siuce', 'estudiante_victima')