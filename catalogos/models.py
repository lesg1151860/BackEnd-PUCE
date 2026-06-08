from django.db import models

class RolCiudadano(models.Model):
    nombre_rol = models.CharField(max_length=255, verbose_name="Nombre del Rol")

    class Meta:
        db_table = 'Rol_Ciudadano'
        verbose_name = 'Rol de Ciudadano'
        verbose_name_plural = 'Roles de Ciudadanos'

    def __str__(self):
        return self.nombre_rol

class EstadoSAC(models.Model):
    estado_sac = models.CharField(max_length=255, verbose_name="Nombre del Estado")

    class Meta:
        db_table = 'Estados_SAC'
        verbose_name = 'Estado SAC'
        verbose_name_plural = 'Estados SAC'

    def __str__(self):
        return self.estado_sac

class RespuestaSAC(models.Model):
    respuesta_sac = models.CharField(max_length=255, verbose_name="Nombre de la Respuesta")

    class Meta:
        db_table = 'Respuestas_SAC'
        verbose_name = 'Respuesta SAC'
        verbose_name_plural = 'Respuestas SAC'

    def __str__(self):
        return self.respuesta_sac

class ClasificacionCaso(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Descripción de la Clasificación")
    
    class Meta:
        db_table = 'Clasificacion_caso'
        verbose_name = 'Clasificación de Caso'
        verbose_name_plural = 'Clasificaciones de Casos'
    
    def __str__(self): 
        return self.descripcion