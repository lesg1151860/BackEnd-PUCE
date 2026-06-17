from django.contrib import admin
from .models import (
    InstitucionEducativa, RolCiudadano, EstadoSAC, RespuestaSAC, ClasificacionCaso,
    TipoIdentificacion, EstadoSIUCE, TipoDano, TipoAgresion,
    EventoGenerador, LugarHechos, GradoEscolaridad, RolAgresor,
    AccionesIE, AccionesSEM
)

# 1. Registramos los modelos simples
@admin.register(RolCiudadano, EstadoSAC, RespuestaSAC, ClasificacionCaso,
                EstadoSIUCE, TipoDano, TipoAgresion, InstitucionEducativa, EventoGenerador,
                LugarHechos, GradoEscolaridad, RolAgresor)
class CatalogoSimpleAdmin(admin.ModelAdmin):
    
    list_display = ('id', '__str__')
    search_fields = ('__str__',)

# 2. Registramos los modelos con campos especiales
@admin.register(TipoIdentificacion)
class TipoIdentificacionAdmin(admin.ModelAdmin):
    list_display = ( 'tipo_identificacion', 'activo')
    list_filter = ('activo',)
    search_fields = ('tipo_identificacion',)

@admin.register(AccionesIE)
class AccionesIEAdmin(admin.ModelAdmin):
    list_display = ('nom_accion_ie', 'porcentaje')
    search_fields = ('nom_accion_ie',)

@admin.register(AccionesSEM)
class AccionesSEMAdmin(admin.ModelAdmin):
    list_display = ('nom_accion_sem', 'porcentaje')
    search_fields = ('nom_accion_sem',)