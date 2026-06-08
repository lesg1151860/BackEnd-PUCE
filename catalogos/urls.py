from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClasificacionCasoViewSet, RolCiudadanoViewSet, EstadoSACViewSet, RespuestaSACViewSet

router = DefaultRouter()
router.register(r'rol_ciudadano', RolCiudadanoViewSet, basename='rol-ciudadano')
router.register(r'estados_sac', EstadoSACViewSet, basename='estado-sac')
router.register(r'respuestas_sac', RespuestaSACViewSet, basename='respuesta-sac')
router.register(r'clasificacion_caso', ClasificacionCasoViewSet, basename='clasificacion-caso')

urlpatterns = [
    path('', include(router.urls)),
]