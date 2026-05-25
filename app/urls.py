# app/urls.py
from django.urls import path
from . import view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    
    # Endpoints de Login (Nuevos)
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Endpoints de Autenticación y Seguridad
    path('api/auth/recuperar-password/', view.solicitar_recuperacion, name='solicitar_recuperacion'),
    path('api/auth/confirmar-password/', view.confirmar_recuperacion, name='confirmar_recuperacion'),
]