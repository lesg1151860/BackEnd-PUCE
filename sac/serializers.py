from rest_framework import serializers
from catalogos.models import EstadoSAC
from .models import CasoSAC 

class CasoSACSerializer(serializers.ModelSerializer):
    
    nombre_lider = serializers.CharField(source='usuario_registro.username', read_only=True)
    
    class Meta:
        model = CasoSAC
        fields = '__all__'
        
        
class EstadoSACSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSAC
        fields = '__all__'

class RespuestaSACSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasoSAC
        fields = ['sac_respuesta']