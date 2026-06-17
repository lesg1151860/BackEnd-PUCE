from rest_framework import viewsets, permissions
from catalogos.models import EstadoSAC
from .models import CasoSAC
from .serializers import CasoSACSerializer, EstadoSACSerializer

class CasoSACViewSet(viewsets.ModelViewSet):
    queryset = CasoSAC.objects.all().order_by('-fecha_radicacion')
    serializer_class = CasoSACSerializer
    
    
class EstadoSACViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EstadoSAC.objects.all()
    serializer_class = EstadoSACSerializer