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
    
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Usuario
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','is_staff') 
        extra_kwargs = {
            'is_staff': {'read_only': True}
        }

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        
        if validated_data.get('is_staff') == True:
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_superuser = False
        user.save()
        return user