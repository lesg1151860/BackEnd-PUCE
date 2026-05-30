# app/siuce/apps.py
from django.apps import AppConfig


class SiuceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.siuce'  # <--- Debe ser 'app.siuce'