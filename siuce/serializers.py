from rest_framework import serializers
from .models import CasoSIUCE
from catalogos.models import (
    TipoIdentificacion, EstadoSIUCE, TipoDano, TipoAgresion,EventoGenerador, LugarHechos,
    GradoEscolaridad, RolAgresor, AccionesIE, AccionesSEM)
from django.contrib.auth import get_user_model

User = get_user_model()

class CasoSIUCESerializer(serializers.ModelSerializer):
    
    usuario_registro_siuce = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = CasoSIUCE
        fields = '__all__'
        read_only_fields = (
            'avance_ie', 
            'avance_sem', 
            'avance_general', 
            'estado',
            'usuario_registro_siuce',
        )

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)  