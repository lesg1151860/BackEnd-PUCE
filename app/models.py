from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Dejamos únicamente los campos personalizados esenciales
    full_name = models.CharField(max_length=255, verbose_name="Nombre Completo")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    def __str__(self):
        return f"{self.username} - {self.full_name}"