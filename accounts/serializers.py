from rest_framework import serializers
from django.contrib.auth import get_user_model # CAMBIA ESTO

User = get_user_model() # CAMBIA ESTO

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Asegúrate de que estos campos existan en app/models.py
        fields = ['id', 'username', 'email', 'first_name', 'last_name']