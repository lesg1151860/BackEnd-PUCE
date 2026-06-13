from django.db import models
from django.conf import settings
from institucion_educativa.models import InstitucionEducativa
from catalogos.models import RolCiudadano, EstadoSAC, RespuestaSAC, ClasificacionCaso

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

    # --- Relaciones (Foreign Keys) ---
    rol_ciudadano = models.ForeignKey(RolCiudadano, on_delete=models.PROTECT, verbose_name="Rol del Ciudadano")
    estado_sac = models.ForeignKey(EstadoSAC, on_delete=models.PROTECT, verbose_name="Estado SAC")
    sac_respuesta = models.ForeignKey(RespuestaSAC, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Respuesta SAC")
    clasificacion = models.ForeignKey(ClasificacionCaso, on_delete=models.PROTECT, verbose_name="Clasificación")
    institucion_1 = models.ForeignKey(InstitucionEducativa, on_delete=models.PROTECT, related_name='casos_institucion_1')
    institucion_2 = models.ForeignKey(InstitucionEducativa, on_delete=models.PROTECT, related_name='casos_institucion_2', null=True, blank=True)
        
    class Meta:
        db_table = 'Caso_SAC'
        verbose_name = "Caso SAC"
        verbose_name_plural = "Casos SAC"

    def __str__(self):
        estado_actual = self.estado_sac.nombre_rol if self.estado_sac else "Sin Estado"
        return f"{self.num_rad_sac} - {self.ciudadano} - {self.estudiante} - {estado_actual}"