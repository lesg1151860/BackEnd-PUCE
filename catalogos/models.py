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

class TipoIdentificacion(models.Model):
    codigo = models.CharField(max_length=100, verbose_name="Código del Tipo de Identificación")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción de la Tipo de Identificación")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        db_table = 'Tipos_Identificacion'
        verbose_name = 'Tipo de Identificación'
        verbose_name_plural = 'Tipos de Identificaciones'
    
    def __str__(self):
        return self.codigo + " - " + self.descripcion

class EstadoSIUCE(models.Model):
    estado_siuce = models.CharField(max_length=255, verbose_name="Nombre del Estado SIUCE")

    class Meta:
        db_table = 'Estados_SIUCE'
        verbose_name = 'Estado SIUCE'
        verbose_name_plural = 'Estados SIUCE'

    def __str__(self):
        return self.estado_siuce

class TipoDano(models.Model):
    tipo_dano = models.CharField(max_length=255, verbose_name="Nombre del Tipo de Daño")

    class Meta:
        db_table = 'Tipos_Dano'
        verbose_name = 'Tipo de Daño'
        verbose_name_plural = 'Tipos de Daños'

    def __str__(self):
        return self.tipo_dano

class TipoAgresion(models.Model):
    tipo_agresion = models.CharField(max_length=255, verbose_name="Nombre del Tipo de Agresión")

    class Meta:
        db_table = 'Tipos_Agresion'
        verbose_name = 'Tipo de Agresión'
        verbose_name_plural = 'Tipos de Agresiones'

    def __str__(self):
        return self.tipo_agresion
        
class EventoGenerador(models.Model):
    evento_generador = models.CharField(max_length=255, verbose_name="Nombre del Evento Generador")

    class Meta:
        db_table = 'Eventos_Generadores'
        verbose_name = 'Evento Generador'
        verbose_name_plural = 'Eventos Generadores'

    def __str__(self):
        return self.evento_generador
    
class LugarHechos(models.Model):
    nom_lugar = models.CharField(max_length=255, verbose_name="Nombre del Lugar de los Hechos")

    class Meta:
        db_table = 'Lugares_Hechos'
        verbose_name = 'Lugar de los Hechos'
        verbose_name_plural = 'Lugares de los Hechos'

    def __str__(self):
        return self.nom_lugar

class GradoEscolaridad(models.Model):
    nom_grado = models.CharField(max_length=255, verbose_name="Nombre del Grado de Escolaridad")

    class Meta:
        db_table = 'Grados_Escolaridad'
        verbose_name = 'Grado de Escolaridad'
        verbose_name_plural = 'Grados de Escolaridad'

    def __str__(self):
        return self.nom_grado
    
class RolAgresor(models.Model):
    nom_rol_agresor = models.CharField(max_length=255, verbose_name="Nombre del Rol del Agresor")

    class Meta:
        db_table = 'Rol_Agresor'
        verbose_name = 'Rol del Agresor'
        verbose_name_plural = 'Roles de Agresores'

    def __str__(self):
        return self.nom_rol_agresor
    
class AccionesIE(models.Model):
    nom_accion_ie = models.CharField(max_length=255, verbose_name="Nombre de la Acción de la Institución Educativa")
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Porcentaje de la Acción")
    
    class Meta:
        db_table = 'Acciones_IE'
        verbose_name = 'Acción de IE'
        verbose_name_plural = 'Acciones de IE'

    def __str__(self):
        return self.nom_accion_ie + " - " + str(self.porcentaje) + "%"

class AccionesSEM(models.Model):
    nom_accion_sem = models.CharField(max_length=255, verbose_name="Nombre de la Acción de la SEM")
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Porcentaje de la Acción")
    
    class Meta:
        db_table = 'Acciones_SEM'
        verbose_name = 'Acción de SEM'
        verbose_name_plural = 'Acciones de SEM'

    def __str__(self):
        return self.nom_accion_sem + " - " + str(self.porcentaje) + "%"