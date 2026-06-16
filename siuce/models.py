from django.db import models
from django.utils import timezone
from catalogos.models import (
    ClasificacionCaso, InstitucionEducativa, TipoDano, TipoIdentificacion, EstadoSIUCE, TipoAgresion, 
    EventoGenerador, LugarHechos, GradoEscolaridad, RolAgresor, 
    AccionesIE, AccionesSEM
)

class CasoSIUCE(models.Model):
    """
    Modelo principal para el Sistema de Información Unificado de Convivencia Escolar.
    """
    
    num_radicado_siuce = models.CharField(max_length=15, verbose_name="Radicado SIUCE")
    avance_general = models.FloatField(default=0.0, verbose_name="Avance Total (%)")
    estado_siuce = models.ForeignKey(EstadoSIUCE, on_delete=models.PROTECT, null=True, verbose_name="Estado SIUCE")
    institucion_educativa = models.ForeignKey(InstitucionEducativa, on_delete=models.PROTECT, verbose_name="Institución Educativa")
    estudiante_victima = models.CharField(max_length=255, verbose_name="Víctima")
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.PROTECT, null=True, verbose_name="Tipo de Identificación")   
    num_indentificacion = models.CharField(max_length=20, verbose_name="Número de Identificación")
    grado_escolaridad = models.ForeignKey(GradoEscolaridad, on_delete=models.PROTECT, null=True, verbose_name="Grado de Escolaridad")
    dano_principal = models.ForeignKey(TipoDano, on_delete=models.RESTRICT, related_name='caso_siuce_dano_principal', null=True, blank=True, verbose_name="Daño Principal")
    dano_secundario = models.ForeignKey(TipoDano, on_delete=models.RESTRICT, related_name='caso_siuce_dano_secundario', null=True, blank=True, verbose_name="Daño Secundario")
    dano_terciario = models.ForeignKey(TipoDano, on_delete=models.RESTRICT, related_name='caso_siuce_dano_terciario', null=True, blank=True, verbose_name="Daño Terciario")
    tipo_agresion = models.ForeignKey(TipoAgresion, on_delete=models.PROTECT, null=True, verbose_name="Tipo de Agresión")
    repetitivo = models.BooleanField(default=False, verbose_name="¿Es Repetitivo?")
    evento_generador = models.ForeignKey(EventoGenerador, on_delete=models.PROTECT, null=True, verbose_name="Evento Generador")
    otro_evento_generador = models.CharField(max_length=255, blank=True, null=True, verbose_name="Otro Evento Generador")
    rol_agresor = models.ForeignKey(RolAgresor, on_delete=models.PROTECT, null=True, verbose_name="Rol del Agresor")
    nombre_agresor = models.CharField(max_length=255, verbose_name="Agresor/Involucrado")
    clasificacion = models.ForeignKey(ClasificacionCaso, on_delete=models.PROTECT, null=True, verbose_name="Clasificación del Caso")
    lugar_hechos = models.ForeignKey(LugarHechos, on_delete=models.PROTECT, null=True, verbose_name="Lugar de los Hechos")
    fecha_ocurrencia = models.DateField(verbose_name="Fecha de Ocurrencia", default=timezone.now)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    seguimiento_ie = models.BooleanField(default=False, verbose_name="En Seguimiento I.E.")
    num_seguimiento_ie = models.CharField(max_length=10, blank=True, null=True, verbose_name="Seguimiento I.E.")
    seguimiento_policia = models.BooleanField(default=False, verbose_name="En Seguimiento Policía")
    num_seguimiento_policia = models.CharField(max_length=10, blank=True, null=True, verbose_name="Seguimiento Policía")
    cec = models.BooleanField(default=False, verbose_name="¿Caso llevado a Comité Curricular?")
    accion_ie = models.ForeignKey(AccionesIE, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Acción I.E.")
    porcentaje_avance_ie = models.FloatField(default=0.0, verbose_name="Porcentaje de Avance I.E.")
    accion_sem = models.ForeignKey(AccionesSEM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Acción S.E.M.")
    porcentaje_avance_sem = models.FloatField(default=0.0, verbose_name="Porcentaje de Avance S.E.M.")
    descripcion_avance = models.TextField(blank=True, null=True, verbose_name="Descripción del Caso")
    rad_entidad_ext = models.CharField(max_length=255, blank=True, null=True, verbose_name="Radicados en Entidades Externas")
    fecha_rad_entidad_ext = models.DateField(blank=True, null=True, verbose_name="Fecha de Radicación en Entidades Externas")
    
    
    class Meta:
        db_table = 'Caso_SIUCE'
        verbose_name = "Caso SIUCE"
        verbose_name_plural = "Casos SIUCE"

    def save(self, *args, **kwargs):
        porcentaje_ie = self.accion_ie.porcentaje if self.accion_ie else 0.0
        porcentaje_sem = self.accion_sem.porcentaje if self.accion_sem else 0.0
        
        self.porcentaje_avance_ie = porcentaje_ie
        self.porcentaje_avance_sem = porcentaje_sem
        self.avance_general = porcentaje_ie + porcentaje_sem
        
        if self.avance_general <= 0:
            nombre_estado = 'PENDIENTE'
        elif 0 < self.avance_general < 100:
            nombre_estado = 'EN SEGUIMIENTO'
        else:
            nombre_estado = 'TERMINADO'
            
        estado_registro = EstadoSIUCE.objects.filter(estado_siuce__iexact=nombre_estado).first()
        
        if estado_registro:
            self.estado_siuce = estado_registro
            
        super().save(*args, **kwargs)

    def __str__(self):

        nombre_visible = self.estado_siuce.estado_siuce if self.estado_siuce else "SIN ESTADO"
        return f"Caso {self.num_radicado_siuce} - {nombre_visible}"