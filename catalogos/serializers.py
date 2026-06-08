from rest_framework import serializers
from .models import ClasificacionCaso, RolCiudadano, EstadoSAC, RespuestaSAC

class RolCiudadanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolCiudadano
        fields = ['id', 'nombre_rol']

class EstadoSACSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSAC
        fields = ['id', 'estado_sac']

class RespuestaSACSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaSAC
        fields = ['id', 'respuesta_sac']

class ClasificacionCasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasificacionCaso
        fields = ['id', 'descripcion']