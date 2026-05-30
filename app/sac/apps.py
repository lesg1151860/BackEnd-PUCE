# app/sac/apps.py
from django.apps import AppConfig


class SacConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.sac'  # <--- Debe ser 'app.sac'