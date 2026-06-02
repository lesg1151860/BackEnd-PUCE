from django.urls import path
from .views import MyTokenObtainPairView, RegistroUsuarioView, UsuarioDetailView, UsuarioListCreateView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # Ruta para obtener el token JWT
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuarios-list-create'), # Ruta para listar y crear usuarios
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuarios-detail'), # Ruta para obtener detalles de un usuario específico
    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'), # Ruta de registro
]