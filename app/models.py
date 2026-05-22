from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Definimos las opciones del Enum usando tuplas para Django
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('lider', 'lider'),
    )
    
    # Heredamos de AbstractUser, el cual ya maneja 'id' automáticamente y 
    # gestiona la contraseña de forma segura (hasheada) internamente.
    full_name = models.CharField(max_length=255, verbose_name="Nombre Completo")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='lider', verbose_name="Rol")

    def __str__(self):
        return f"{self.username} - {self.role}"