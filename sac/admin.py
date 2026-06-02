from django.contrib import admin
from .models import (
    RolCiudadano, EstadoSAC, SACRespuesta, 
    Clasificacion, InstitucionEducativa, CasoSAC
)

@admin.register(RolCiudadano)
class RolCiudadanoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(EstadoSAC)
class EstadoSACAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(SACRespuesta)
class SACRespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(InstitucionEducativa)
class InstitucionEducativaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_oficial', 'sector')
    list_filter = ('sector',)
    search_fields = ('nombre_oficial',)

@admin.register(CasoSAC)
class CasoSACAdmin(admin.ModelAdmin):
    # Campos que se muestran en la tabla principal
    list_display = (
        'num_rad_sac', 'ciudadano', 'estudiante', 
        'fecha_radicacion', 'estado_sac', 'clasificacion'
    )
    
    # Filtros laterales para búsqueda rápida
    list_filter = ('estado_sac', 'clasificacion', 'traslado_ie', 'respondido')
    
    # Barra de búsqueda
    search_fields = ('num_rad_sac', 'ciudadano', 'estudiante')
    
    # Para mejorar la experiencia en formularios largos, puedes agrupar campos
    fieldsets = (
        ('Información General', {
            'fields': ('num_rad_sac', 'ciudadano', 'estudiante', 'fecha_radicacion')
        }),
        ('Seguimiento y Radicados', {
            'fields': (
                'radicado_respuesta', 'radicado_externa', 'num_radicado_traslado', 
                'radicado_prorroga', 'radicado_contestacion'
            )
        }),
        ('Estados y Flags', {
            'fields': (
                'traslado_ie', 'respondido', 'prorroga', 
                'fecha_nueva_prorroga', 'contestacion_ie'
            )
        }),
        ('Relaciones y Catálogos', {
            'fields': (
                'rol_ciudadano', 'estado_sac', 'sac_respuesta', 
                'clasificacion', 'institucion_1', 'institucion_2', 'usuario'
            )
        }),
    )