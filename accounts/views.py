from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from accounts.models import Usuario
from .serializers import MyTokenObtainPairSerializer, RegistroUsuarioSerializer

# --- Vista personalizada para obtener el token JWT con información adicional ---
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# --- Vista para listar y crear usuarios ---
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer
           
# --- Vista de Registro ---
class RegistroUsuarioView(generics.CreateAPIView):
     queryset = Usuario.objects.all()
     permission_classes = (AllowAny,) # AllowAny permite que cualquiera se registre. 
     serializer_class = RegistroUsuarioSerializer

# --- Vista de Detalle, Actualización y Eliminación de Usuario ---
class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [AllowAny]    
