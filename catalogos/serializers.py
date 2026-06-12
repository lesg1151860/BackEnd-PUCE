from rest_framework import serializers
from .models import (
    RolCiudadano, EstadoSAC, RespuestaSAC, ClasificacionCaso, 
    TipoIdentificacion, EstadoSIUCE, TipoDano, TipoAgresion, 
    EventoGenerador, LugarHechos, GradoEscolaridad, RolAgresor, 
    AccionesIE, AccionesSEM
)

class ClasificacionCasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasificacionCaso
        fields = '__all__'
        
# --- Catálogos SAC ---
class RolCiudadanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolCiudadano
        fields = '__all__'

class EstadoSACSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSAC
        fields = '__all__'

class RespuestaSACSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaSAC
        fields = '__all__'

# --- Catálogos SIUCE ---
class TipoIdentificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIdentificacion
        fields = '__all__'

class EstadoSIUCESerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSIUCE
        fields = '__all__'

class TipoDanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDano
        fields = '__all__'

class TipoAgresionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAgresion
        fields = '__all__'

class EventoGeneradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoGenerador
        fields = '__all__'

class LugarHechosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LugarHechos
        fields = '__all__'

class GradoEscolaridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradoEscolaridad
        fields = '__all__'

class RolAgresorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolAgresor
        fields = '__all__'

class AccionesIESerializer(serializers.ModelSerializer):
    class Meta:
        model = AccionesIE
        fields = '__all__'

class AccionesSEMSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccionesSEM
        fields = '__all__'