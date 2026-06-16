from rest_framework import serializers
from .models import (
    InstitucionEducativa, InstitucionEducativa, RolCiudadano, EstadoSAC, RespuestaSAC, ClasificacionCaso, 
    TipoIdentificacion, EstadoSIUCE, TipoDano, TipoAgresion, 
    EventoGenerador, LugarHechos, GradoEscolaridad, RolAgresor, 
    AccionesIE, AccionesSEM
)

class InstitucionEducativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitucionEducativa
        fields = '__all__'
        
class ClasificacionCasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasificacionCaso
        fields = '__all__'

    def validate_descripcion(self, value):
        # 1. Limpiamos espacios al inicio y final
        descripcion_limpia = value.strip()
        
        # 2. Buscamos registros existentes que sean iguales ignorando mayúsculas/minúsculas
        # Usamos exclude para ignorar el objeto actual si estamos en modo edición
        query = ClasificacionCaso.objects.filter(descripcion__iexact=descripcion_limpia)
        
        if self.instance:
            query = query.exclude(id=self.instance.id)
            
        if query.exists():
            raise serializers.ValidationError("Ya existe una clasificación con este nombre.")
            
        return descripcion_limpia
    
# --- Catálogos SAC ---
class RolCiudadanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolCiudadano
        fields = '__all__'

    def validate_nombre_rol(self, value):
        nombre_limpio = value.strip()
        query = RolCiudadano.objects.filter(nombre_rol__iexact=nombre_limpio)
        
        if self.instance:
            query = query.exclude(id=self.instance.id)
            
        if query.exists():
            raise serializers.ValidationError("Ya existe un rol registrado con este nombre.")
            
        return nombre_limpio

class EstadoSACSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSAC
        fields = '__all__'

    def validate_estado_sac(self, value):
        nombre_limpio = value.strip()
        query = EstadoSAC.objects.filter(estado_sac__iexact=nombre_limpio)
        if self.instance:
            query = query.exclude(id=self.instance.id)
        if query.exists():
            raise serializers.ValidationError("Ya existe un estado con este nombre.")
        return nombre_limpio

class RespuestaSACSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaSAC
        fields = '__all__'

    def validate_respuesta_sac(self, value):
        nombre_limpio = value.strip()
        query = RespuestaSAC.objects.filter(respuesta_sac__iexact=nombre_limpio)
        if self.instance:
            query = query.exclude(id=self.instance.id)
        if query.exists():
            raise serializers.ValidationError("Ya existe una respuesta con este nombre.")
        return nombre_limpio

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