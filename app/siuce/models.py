from django.db import models

class CasoSIUCE(models.Model):
    radicado = models.IntegerField(primary_key=True)
    avance_ie = models.FloatField(default=0.0)
    avance_sem = models.FloatField(default=0.0)
    avance_general = models.FloatField(default=0.0, editable=False)
    estado = models.CharField(max_length=20, default='PENDIENTE', editable=False)
    tipo_agresion = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10) # Tipo 1, 2, 3
    
    def save(self, *args, **kwargs):
        # 1. El campo “Avance General” es la SUMA de “Avance IE” + “Avance SEM”
        self.avance_general = self.avance_ie + self.avance_sem

        # 2. El campo “Estado” debe ser AUTOMÁTICO según el Avance General
        if self.avance_general <= 0:
            self.estado = 'PENDIENTE'
        elif 0 < self.avance_general < 100:
            self.estado = 'EN SEGUIMIENTO'
        else:
            self.estado = 'TERMINADO'
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Caso {self.radicado} - {self.estado}"