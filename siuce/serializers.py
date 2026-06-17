from rest_framework import serializers
from .models import CasoSIUCE
# Importamos los modelos de catálogo para asegurar que existan las relaciones
from catalogos.models import (
    TipoIdentificacion, EstadoSIUCE, TipoDano, TipoAgresion, 
    EventoGenerador, LugarHechos, GradoEscolaridad, RolAgresor, 
    AccionesIE, AccionesSEM
)

class CasoSIUCESerializer(serializers.ModelSerializer):
    """
    Serializer para CasoSIUCE que maneja todas las relaciones de catálogos.
    """
    
    class Meta:
        model = CasoSIUCE
        fields = '__all__'
        read_only_fields = (
            'avance_ie', 
            'avance_sem', 
            'avance_general', 
            'estado', 
            'fecha_registro'
        )

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)