from django.db import models
from catalogos.models import (
    TipoIdentificacion, EstadoSIUCE, TipoDano, TipoAgresion, 
    EventoGenerador, LugarHechos, GradoEscolaridad, RolAgresor, 
    AccionesIE, AccionesSEM
)

class CasoSIUCE(models.Model):
    """
    Modelo principal para el Sistema de Información Unificado de Convivencia Escolar.
    """
    radicado_sac = models.CharField(max_length=50, verbose_name="Radicado SAC asociado")
    estudiante_victima = models.CharField(max_length=255, verbose_name="Víctima")
    nombre_agresor = models.CharField(max_length=255, verbose_name="Agresor/Involucrado")

    # --- Relaciones con Catálogos (catalogos.models) ---
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.PROTECT, null=True, verbose_name="Tipo de Identificación")
    estado_siuce = models.ForeignKey(EstadoSIUCE, on_delete=models.PROTECT, null=True, verbose_name="Estado SIUCE")
    grado_escolaridad = models.ForeignKey(GradoEscolaridad, on_delete=models.PROTECT, null=True, verbose_name="Grado de Escolaridad")
    tipo_agresion = models.ForeignKey(TipoAgresion, on_delete=models.PROTECT, null=True, verbose_name="Tipo de Agresión")
    evento_generador = models.ForeignKey(EventoGenerador, on_delete=models.PROTECT, null=True, verbose_name="Evento Generador")
    rol_agresor = models.ForeignKey(RolAgresor, on_delete=models.PROTECT, null=True, verbose_name="Rol del Agresor")
    lugar_hechos = models.ForeignKey(LugarHechos, on_delete=models.PROTECT, null=True, verbose_name="Lugar de los Hechos")
    
    # Acciones con porcentajes (calculados en save)
    accion_ie = models.ForeignKey(AccionesIE, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Acción I.E.")
    accion_sem = models.ForeignKey(AccionesSEM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Acción S.E.M.")
    
    # Relación muchos a muchos para daños
    tipos_dano = models.ManyToManyField(TipoDano, verbose_name="Tipos de Daño")

    # --- Otros Campos ---
    avance_ie = models.FloatField(default=0.0, verbose_name="Avance I.E.")
    avance_sem = models.FloatField(default=0.0, verbose_name="Avance S.E.M.")
    avance_general = models.FloatField(default=0.0, verbose_name="Avance Total (%)")
    estado = models.CharField(max_length=20, default='PENDIENTE', verbose_name="Estado del Caso")
    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

class Meta:
    db_table = 'Caso_SIUCE' # Renombrado según tu solicitud
    verbose_name = "Caso SIUCE"
    verbose_name_plural = "Casos SIUCE"

    def save(self, *args, **kwargs):
        porcentaje_ie = self.accion_ie.porcentaje if self.accion_ie else 0.0
        porcentaje_sem = self.accion_sem.porcentaje if self.accion_sem else 0.0
        
        self.avance_ie = porcentaje_ie
        self.avance_sem = porcentaje_sem
        self.avance_general = porcentaje_ie + porcentaje_sem
        
        if self.avance_general <= 0:
            self.estado = 'PENDIENTE'
        elif 0 < self.avance_general < 100:
            self.estado = 'EN SEGUIMIENTO'
        else:
            self.estado = 'TERMINADO'
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Caso {self.radicado_sac} - {self.estado}"