from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    ClasificacionCaso, RolCiudadano, EstadoSAC, RespuestaSAC,
    TipoIdentificacion, EstadoSIUCE, TipoDano, TipoAgresion,
    EventoGenerador, LugarHechos, GradoEscolaridad, RolAgresor,
    AccionesIE, AccionesSEM
)
from .serializers import (
    ClasificacionCasoSerializer, RolCiudadanoSerializer, EstadoSACSerializer, 
    RespuestaSACSerializer, TipoIdentificacionSerializer, EstadoSIUCESerializer, 
    TipoDanoSerializer, TipoAgresionSerializer, EventoGeneradorSerializer, 
    LugarHechosSerializer, GradoEscolaridadSerializer, RolAgresorSerializer, 
    AccionesIESerializer, AccionesSEMSerializer
)

# --- ViewSets SAC ---
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

# --- ViewSets SIUCE ---
class TipoIdentificacionViewSet(viewsets.ModelViewSet):
    queryset = TipoIdentificacion.objects.all().order_by('id')
    serializer_class = TipoIdentificacionSerializer
    permission_classes = [IsAuthenticated]

class EstadoSIUCEViewSet(viewsets.ModelViewSet):
    queryset = EstadoSIUCE.objects.all().order_by('id')
    serializer_class = EstadoSIUCESerializer
    permission_classes = [IsAuthenticated]

class TipoDanoViewSet(viewsets.ModelViewSet):
    queryset = TipoDano.objects.all().order_by('id')
    serializer_class = TipoDanoSerializer
    permission_classes = [IsAuthenticated]

class TipoAgresionViewSet(viewsets.ModelViewSet):
    queryset = TipoAgresion.objects.all().order_by('id')
    serializer_class = TipoAgresionSerializer
    permission_classes = [IsAuthenticated]

class EventoGeneradorViewSet(viewsets.ModelViewSet):
    queryset = EventoGenerador.objects.all().order_by('id')
    serializer_class = EventoGeneradorSerializer
    permission_classes = [IsAuthenticated]

class LugarHechosViewSet(viewsets.ModelViewSet):
    queryset = LugarHechos.objects.all().order_by('id')
    serializer_class = LugarHechosSerializer
    permission_classes = [IsAuthenticated]

class GradoEscolaridadViewSet(viewsets.ModelViewSet):
    queryset = GradoEscolaridad.objects.all().order_by('id')
    serializer_class = GradoEscolaridadSerializer
    permission_classes = [IsAuthenticated]

class RolAgresorViewSet(viewsets.ModelViewSet):
    queryset = RolAgresor.objects.all().order_by('id')
    serializer_class = RolAgresorSerializer
    permission_classes = [IsAuthenticated]

class AccionesIEViewSet(viewsets.ModelViewSet):
    queryset = AccionesIE.objects.all().order_by('id')
    serializer_class = AccionesIESerializer
    permission_classes = [IsAuthenticated]

class AccionesSEMViewSet(viewsets.ModelViewSet):
    queryset = AccionesSEM.objects.all().order_by('id')
    serializer_class = AccionesSEMSerializer
    permission_classes = [IsAuthenticated]