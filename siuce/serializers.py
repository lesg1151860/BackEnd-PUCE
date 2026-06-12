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
        
        # Estos campos son calculados automáticamente en el método save() del modelo,
        # por lo tanto, el usuario no debe poder enviarlos ni modificarlos directamente.
        read_only_fields = (
            'avance_ie', 
            'avance_sem', 
            'avance_general', 
            'estado', 
            'fecha_registro'
        )

    # Nota: Si en el futuro necesitas que el frontend envíe el ID pero reciba el objeto completo 
    # (por ejemplo, ver el nombre del Tipo de Daño en lugar de solo el número), 
    # puedes añadir campos como estos:
    # tipo_identificacion_data = serializers.SerializerMethodField()

    def update(self, instance, validated_data):
        # Al llamar a super().update(), Django procesa los datos y llama a save() del modelo,
        # lo que garantiza que los porcentajes y el estado se recalculen correctamente.
        return super().update(instance, validated_data)