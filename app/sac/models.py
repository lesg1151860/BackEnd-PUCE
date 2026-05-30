from django.db import models

class TipoIdentificacion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class SolicitudSAC(models.Model):
    radicado = models.CharField(max_length=20, primary_key=True, help_text="Formato: CUCYYYYER######")
    ciudadano = models.CharField(max_length=255)
    fecha_radicacion = models.DateField()
    radicado_respuesta = models.CharField(max_length=20, blank=True, null=True)
    
    # Ejemplo de uso de Choices para mayor integridad
    ROL_CHOICES = [
        ('EST', 'Estudiante'), ('DOC', 'Docente'), ('ADM', 'Administrativo'), ('PAD', 'Padre de Familia')
    ]
    rol = models.CharField(max_length=3, choices=ROL_CHOICES)
    
    traslado_ie = models.BooleanField(default=False)
    ie_destino = models.CharField(max_length=255, blank=True, null=True)
    radicado_traslado = models.CharField(max_length=20, blank=True, null=True)
    radicado_externa = models.CharField(max_length=20, blank=True, null=True)
    
    respondido = models.BooleanField(default=False)
    prorroga = models.BooleanField(default=False)
    fecha_nueva_prorroga = models.DateField(blank=True, null=True)
    radicado_prorroga = models.CharField(max_length=20, blank=True, null=True)
    contestacion_ie = models.BooleanField(default=False)
    radicado_contestacion = models.CharField(max_length=20, blank=True, null=True)
    
    estudiante = models.CharField(max_length=255)
    institucion_involucrada = models.CharField(max_length=255)
    situacion = models.CharField(max_length=10) # Tipo 1, 2, 3
    
    SAC_RESPUESTA_CHOICES = [('ENV', 'ENVIADA'), ('NO', 'NO'), ('SI', 'SÍ')]
    sac_respuesta = models.CharField(max_length=3, choices=SAC_RESPUESTA_CHOICES)
    
    ESTADO_CHOICES = [('SEG', 'EN SEGUIMIENTO'), ('TER', 'TERMINADO')]
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES)

    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.SET_NULL, null=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Radicado: {self.radicado}"