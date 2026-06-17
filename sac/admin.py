from django.contrib import admin
from .models import CasoSAC

@admin.register(CasoSAC)
class CasoSACAdmin(admin.ModelAdmin):

    list_display = (
        'num_radicado_sac', 
        'ciudadano', 
        'estudiante', 
        'fecha_radicacion', 
        'rol_ciudadano', 
        'estado_sac', 
        'respondido'
    )
    
    list_display_links = ('num_radicado_sac', 'ciudadano')
    
    search_fields = ('num_radicado_sac', 'ciudadano', 'estudiante')
    
    list_filter = (
        'estado_sac', 
        'respondido', 
        'prorroga', 
        'rol_ciudadano', 
        'fecha_radicacion', 
        'institucion_1'
    )
    
    fieldsets = (
        ('Información Básica del Radicado', {
            'fields': (
                'num_radicado_sac', 
                'fecha_radicacion', 
                'estado_sac'
            )
        }),
        ('Información de los Implicados', {
            'fields': (
                'ciudadano', 
                'rol_ciudadano', 
                'estudiante'
            )
        }),
        ('Detalles de la Clasificación e Instituciones', {
            'fields': (
                'clasificacion', 
                'institucion_1', 
                'traslado_ie', 
                'institucion_2', 
                'num_radicado_traslado'
            )
        }),
        ('Gestión de Prórrogas y Respuestas', {
            'fields': (
                'prorroga', 
                'fecha_nueva_prorroga', 
                'radicado_prorroga',
                'contestacion_ie', 
                'radicado_contestacion_ie',
                'respondido', 
                'radicado_respuesta', 
                'sac_respuesta'
            )
        }),
    )

    raw_id_fields = ('institucion_1', 'institucion_2')