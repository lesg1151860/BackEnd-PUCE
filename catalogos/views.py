from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ClasificacionCaso, RolCiudadano, EstadoSAC, RespuestaSAC
from .serializers import ClasificacionCasoSerializer, RolCiudadanoSerializer, EstadoSACSerializer, RespuestaSACSerializer

class RolCiudadanoViewSet(viewsets.ModelViewSet):
    queryset = RolCiudadano.objects.all().order_by('id')
    serializer_class = RolCiudadanoSerializer
    permission_classes = [IsAuthenticated]

class EstadoSACViewSet(viewsets.ModelViewSet):
    queryset = EstadoSAC.objects.all().order_by('id')
    serializer_class = EstadoSACSerializer
    permission_classes = [IsAuthenticated]

class RespuestaSACViewSet(viewsets.ModelViewSet):
    queryset = RespuestaSAC.objects.all().order_by('id')
    serializer_class = RespuestaSACSerializer
    permission_classes = [IsAuthenticated]
    
class ClasificacionCasoViewSet(viewsets.ModelViewSet):
    queryset = ClasificacionCaso.objects.all().order_by('id')
    serializer_class = ClasificacionCasoSerializer
    permission_classes = [IsAuthenticated]