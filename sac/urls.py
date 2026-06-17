from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CasoSACViewSet, EstadoSACViewSet

router = DefaultRouter()
router.register(r'casos-sac', CasoSACViewSet)
router.register(r'estados_sac', EstadoSACViewSet)

urlpatterns = [
    path('', include(router.urls)),
]