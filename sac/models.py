from django.db import models
from django.conf import settings
from catalogos.models import InstitucionEducativa
from catalogos.models import RolCiudadano, EstadoSAC, RespuestaSAC, ClasificacionCaso
from django.utils import timezone
from django.contrib.auth import get_user_model

# --- Modelo Principal: Caso SAC ---
class CasoSAC(models.Model):
    
    num_radicado_sac = models.CharField(max_length=15, verbose_name="Radicado SIUCE", unique=True)
    ciudadano = models.CharField(max_length=255)
    fecha_radicacion = models.DateField(verbose_name="Fecha de Ocurrencia", default=timezone.now)
    radicado_respuesta = models.CharField(max_length=50, blank=True, null=True , unique=True)
    rol_ciudadano = models.ForeignKey(RolCiudadano, on_delete=models.PROTECT, verbose_name="Rol del Ciudadano")
    estudiante = models.CharField(max_length=255, verbose_name="Nombre Estudiante")
    institucion_1 = models.ForeignKey(InstitucionEducativa, on_delete=models.PROTECT, related_name='casos_institucion_1', blank=True, null=True)
    traslado_ie = models.BooleanField(default=False, verbose_name="Traslado IE", blank=True, null=True)
    institucion_2 = models.ForeignKey(InstitucionEducativa, on_delete=models.PROTECT, related_name='casos_institucion_2', null=True, blank=True)
    num_radicado_traslado = models.CharField(max_length=50, blank=True, null=True, unique=True)
    radicado_externa = models.CharField(max_length=50, blank=True, null=True, unique=True)
    respondido = models.BooleanField(default=False, verbose_name="¿Respondido?")
    prorroga = models.BooleanField(default=False, verbose_name="¿Prórroga?")
    fecha_nueva_prorroga = models.DateField(blank=True, null=True, verbose_name="Fecha Nueva Prórroga")
    radicado_prorroga = models.CharField(max_length=50, blank=True, null=True, verbose_name="Radicado Prórroga")
    contestacion_ie = models.BooleanField(default=False, verbose_name="Contestación IE") 
    radicado_contestacion_ie= models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name="Radicado Contestación IE")
    clasificacion = models.ForeignKey(ClasificacionCaso, on_delete=models.PROTECT, verbose_name="Clasificación del Caso")  
    estado_sac = models.ForeignKey(EstadoSAC, on_delete=models.PROTECT, verbose_name="Estado SAC")
    sac_respuesta = models.ForeignKey(RespuestaSAC, on_delete=models.SET_NULL,  null=True, blank=True, verbose_name="Respuesta SAC")
    usuario_registro = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='casos_sac_registrados', verbose_name="Registrado por", null=True, blank=True)
        
    class Meta:
        db_table = 'Caso_SAC'
        verbose_name = "Caso SAC"
        verbose_name_plural = "Casos SAC"

    def __str__(self):
        estado_actual = self.estado_sac.nombre_rol if self.estado_sac else "Sin Estado"
        return f"{self.num_radicado_sac} - {self.ciudadano} - {self.estudiante} - {estado_actual}"