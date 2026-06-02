from django.db import models

class InstitucionEducativa(models.Model):
    SECTOR_CHOICES = [
        ('PUBLICA', 'Pública'),
        ('PRIVADA', 'Privada'),
    ]

    nombre = models.CharField(max_length=255, verbose_name="Nombre de la Institución")
    sector = models.CharField(max_length=10, choices=SECTOR_CHOICES, default='PUBLICA')
    rector = models.CharField(max_length=255, verbose_name="Nombre del Rector")
    num_contacto = models.CharField(max_length=50, verbose_name="Número de Contacto", blank=True, null=True)

    class Meta:
        verbose_name = 'Institución Educativa'
        verbose_name_plural = 'Instituciones Educativas'
        ordering = ['nombre'] # Ordena alfabéticamente por defecto

    def __str__(self):
        return f"{self.nombre} - {self.get_sector_display()} - {self.rector}"