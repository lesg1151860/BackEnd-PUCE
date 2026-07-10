from rest_framework import viewsets
from .models import CasoSIUCE
from .serializers import CasoSIUCESerializer

class CasoSIUCEViewSet(viewsets.ModelViewSet):
    queryset = CasoSIUCE.objects.all()
    serializer_class = CasoSIUCESerializer

    def perform_create(self, serializer):
        serializer.save(usuario_registro_siuce=self.request.user)