from rest_framework import viewsets, permissions
from catalogos.models import EstadoSAC
from .models import CasoSAC
from .serializers import CasoSACSerializer, EstadoSACSerializer, RespuestaSACSerializer

class CasoSACViewSet(viewsets.ModelViewSet):
    queryset = CasoSAC.objects.all().order_by('-fecha_radicacion')
    serializer_class = CasoSACSerializer
    def perform_create(self, serializer):
        serializer.save(usuario_registro=self.request.user)
    
class EstadoSACViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstadoSAC.objects.all()
    serializer_class = EstadoSACSerializer
    
class RespuestaSACViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CasoSAC.objects.all()
    serializer_class = RespuestaSACSerializer