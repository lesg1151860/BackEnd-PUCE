from django.db import models

class CatalogoAccionIE(models.Model):
    """Catálogo para acciones de Institución Educativa."""
    descripcion = models.CharField(max_length=255, verbose_name="Descripción de la acción")
    porcentaje = models.FloatField(help_text="Porcentaje de avance asociado (ej: 12.5)")

    def __str__(self):
        return f"{self.descripcion} ({self.porcentaje}%)"

class TipoAgresion(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class TipoDano(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class EventoGenerador(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class ClasificacionLey1620(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __str__(self): return f"{self.tipo}: {self.descripcion[:30]}..."

class CatalogoAccionSEM(models.Model):
    descripcion = models.CharField(max_length=255)
    porcentaje = models.FloatField()
    def __str__(self): return f"{self.descripcion} ({self.porcentaje}%)"

class CasoSIUCE(models.Model):
    """
    Modelo principal para el Sistema de Información Unificado de Convivencia Escolar.
    """
    radicado_sac = models.CharField(max_length=50, verbose_name="Radicado SAC asociado")
        
    estudiante_victima = models.CharField(max_length=255, verbose_name="Víctima")
    nombre_agresor = models.CharField(max_length=255, verbose_name="Agresor/Involucrado")
    
    # Relaciones con los catálogos
    accion_ie = models.ForeignKey(CatalogoAccionIE, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Acción I.E.")
    accion_sem = models.ForeignKey(CatalogoAccionSEM, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Acción S.E.M.")
    tipo_agresion = models.ForeignKey(TipoAgresion, on_delete=models.SET_NULL, null=True)
    evento_generador = models.ForeignKey(EventoGenerador, on_delete=models.SET_NULL, null=True)
    clasificacion = models.ForeignKey(ClasificacionLey1620, on_delete=models.SET_NULL, null=True)
    
    # Campos calculados
    avance_ie = models.FloatField(default=0.0, verbose_name="Avance I.E.")
    avance_sem = models.FloatField(default=0.0, verbose_name="Avance S.E.M.")
    avance_general = models.FloatField(default=0.0, verbose_name="Avance Total (%)")
    estado = models.CharField(max_length=20, default='PENDIENTE', verbose_name="Estado del Caso")
    
    tipos_dano = models.ManyToManyField(TipoDano, verbose_name="Tipos de Daño")
    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'caso_siuce'

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