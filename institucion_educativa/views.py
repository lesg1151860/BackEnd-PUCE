from rest_framework import generics
from .models import InstitucionEducativa
from .serializers import InstitucionEducativaSerializer

class InstitucionListCreateView(generics.ListCreateAPIView):
    queryset = InstitucionEducativa.objects.all()
    serializer_class = InstitucionEducativaSerializer
    # permission_classes = [IsAuthenticated] # Descomenta para proteger la ruta

class InstitucionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstitucionEducativa.objects.all()
    serializer_class = InstitucionEducativaSerializer
    # permission_classes = [IsAuthenticated]