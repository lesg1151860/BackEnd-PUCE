from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from accounts.models import Usuario
from .serializers import MyTokenObtainPairSerializer, RegistroUsuarioSerializer, CambiarPasswordSerializer

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

# --- Vista para cambiar la contraseña de un usuario ---
class CambiarPasswordView(generics.GenericAPIView):
    queryset = Usuario.objects.all()
    serializer_class = CambiarPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            if not user.check_password(serializer.validated_data.get("password_actual")):
                return Response(
                    {"password_actual": ["La contraseña actual es incorrecta."]}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.set_password(serializer.validated_data.get("nueva_password"))
            user.save()
            
            return Response(
                {"detail": "Contraseña actualizada correctamente."}, 
                status=status.HTTP_200_OK
            )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)