from rest_framework import viewsets, permissions
from .models import CasoSIUCE
from .serializers import CasoSIUCESerializer

class CasoSIUCEViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los casos del SIUCE.
    """
    queryset = CasoSIUCE.objects.all().order_by('-fecha_registro')
    serializer_class = CasoSIUCESerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Aquí puedes añadir lógica adicional antes de guardar si lo necesitas
        serializer.save()

    def perform_update(self, serializer):
        # Esto asegura que el método save() del modelo se ejecute al actualizar,
        # lo que dispara los cálculos de porcentaje y estado automáticamente.
        serializer.save()