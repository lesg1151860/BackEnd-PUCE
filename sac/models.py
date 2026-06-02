from django.db import models
from django.conf import settings
from institucion_educativa.models import InstitucionEducativa

# --- Catálogos ---

class RolCiudadano(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.descripcion

class EstadoSAC(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.descripcion

class SACRespuesta(models.Model):
    descripcion = models.TextField()
    
    def __str__(self): 
        return self.descripcion

class Clasificacion(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.descripcion

# --- Modelo Principal: Caso SAC ---
class CasoSAC(models.Model):
    # PK
    num_rad_sac = models.CharField(max_length=50, primary_key=True, verbose_name="Número Radicado")
    
    # Datos básicos
    ciudadano = models.CharField(max_length=255)
    estudiante = models.CharField(max_length=255, verbose_name="Nombre Estudiante")
    fecha_radicacion = models.DateField()
    
    # Radicados y control
    radicado_respuesta = models.CharField(max_length=50, blank=True, null=True)
    radicado_externa = models.CharField(max_length=50, blank=True, null=True)
    num_radicado_traslado = models.CharField(max_length=50, blank=True, null=True)
    radicado_prorroga = models.CharField(max_length=50, blank=True, null=True)
    radicado_contestacion = models.CharField(max_length=50, blank=True, null=True)
    
    # Flags (Booleanos)
    traslado_ie = models.BooleanField(default=False, verbose_name="Traslado IE")
    respondido = models.BooleanField(default=False)
    prorroga = models.BooleanField(default=False)
    contestacion_ie = models.BooleanField(default=False)
    
    # Fechas
    fecha_nueva_prorroga = models.DateField(blank=True, null=True)

    # Relaciones (Foreign Keys)
    rol_ciudadano = models.ForeignKey(RolCiudadano, on_delete=models.PROTECT)
    estado_sac = models.ForeignKey(EstadoSAC, on_delete=models.PROTECT)
    sac_respuesta = models.ForeignKey(SACRespuesta, on_delete=models.SET_NULL, null=True, blank=True)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.PROTECT)
    
    # Instituciones (Mapeando Id_Institucion_1 e Id_Institucion_2 al nuevo modelo importado)
    institucion_1 = models.ForeignKey(InstitucionEducativa, on_delete=models.PROTECT, related_name='casos_institucion_1')
    institucion_2 = models.ForeignKey(InstitucionEducativa, on_delete=models.PROTECT, related_name='casos_institucion_2', null=True, blank=True)
        
    class Meta:
        verbose_name = "Caso SAC"
        verbose_name_plural = "Casos SAC"

    def __str__(self):
        return f"{self.num_rad_sac} - {self.ciudadano} - {self.estudiante} - {self.estado_sac} - {self.clasificacion}"