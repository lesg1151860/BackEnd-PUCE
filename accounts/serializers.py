from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Usuario

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = "ADMINISTRADOR" if self.user.is_staff else "LIDER"
        return data

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    
    is_staff = serializers.BooleanField(required=False)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Usuario
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','is_staff') 

    def create(self, validated_data):
        es_admin = validated_data.pop('is_staff', False)
        password = validated_data.pop('password')
        
        user = Usuario(**validated_data)
        user.set_password(password)
        
        if es_admin:
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_superuser = False
            
        user.save()
        return user