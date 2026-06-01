from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model # CAMBIA ESTO

User = get_user_model() # CAMBIA ESTO

class UsuarioListView(APIView):
    def get(self, request):
        users = User.objects.all() # Ahora esto funcionará
        from .serializers import UserSerializer
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)