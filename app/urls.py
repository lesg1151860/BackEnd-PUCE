# app/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import view
from .admin_views import UserAdminViewSet


router = DefaultRouter()
router.register(r'api/admin/users', UserAdminViewSet, basename='admin-users')

urlpatterns = [
    # Endpoints de Login (Nuevos)
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Endpoints de Autenticación y Seguridad
    path('api/auth/recuperar-password/', view.solicitar_recuperacion, name='solicitar_recuperacion'),
    path('api/auth/confirmar-password/', view.confirmar_recuperacion, name='confirmar_recuperacion'),

    # CRUD administrativo de usuarios
    path('', include(router.urls)),
]