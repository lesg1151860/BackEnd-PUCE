from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Administrador'
    LIDER = 'lider', 'Líder'

class User(AbstractUser):
    # Dejamos únicamente los campos personalizados esenciales
    full_name = models.CharField(max_length=255, verbose_name="Nombre Completo")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.LIDER,
        verbose_name="Rol",
    )

    def save(self, *args, **kwargs):
        if self.role == UserRole.ADMIN:
            self.is_staff = True
        elif not self.is_superuser:
            self.is_staff = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.full_name}"