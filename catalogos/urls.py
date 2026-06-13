from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RolCiudadanoViewSet, EstadoSACViewSet, RespuestaSACViewSet, 
    ClasificacionCasoViewSet, TipoIdentificacionViewSet, EstadoSIUCEViewSet,
    TipoDanoViewSet, TipoAgresionViewSet, EventoGeneradorViewSet,
    LugarHechosViewSet, GradoEscolaridadViewSet, RolAgresorViewSet,
    AccionesIEViewSet, AccionesSEMViewSet
)

router = DefaultRouter()

# Registro de rutas para catálogos SAC y SIUCE
router.register(r'rol_ciudadano', RolCiudadanoViewSet)
router.register(r'estado_sac', EstadoSACViewSet)
router.register(r'respuesta_sac', RespuestaSACViewSet)
router.register(r'clasificacion_caso', ClasificacionCasoViewSet)
router.register(r'tipo_identificacion', TipoIdentificacionViewSet)
router.register(r'estado_siuce', EstadoSIUCEViewSet)
router.register(r'tipo_dano', TipoDanoViewSet)
router.register(r'tipo_agresion', TipoAgresionViewSet)
router.register(r'evento_generador', EventoGeneradorViewSet)
router.register(r'lugar_hechos', LugarHechosViewSet)
router.register(r'grado_escolaridad', GradoEscolaridadViewSet)
router.register(r'rol_agresor', RolAgresorViewSet)
router.register(r'acciones_ie', AccionesIEViewSet)
router.register(r'acciones_sem', AccionesSEMViewSet)

urlpatterns = [
    path('', include(router.urls)),
]