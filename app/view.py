# app/views.py
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from .models import User

# --- LOGIN ---
@api_view(['POST'])
def login_view(request):
    username_or_email = request.data.get('username')
    password = request.data.get('password')

    if not username_or_email or not password:
        return Response({"error": "Faltan credenciales"}, status=status.HTTP_400_BAD_REQUEST)

    # 1. Intentar autenticar primero asumiendo que es username
    user = authenticate(username=username_or_email, password=password)
    
    # 2. Si falla, intentar buscar por email
    if user is None:
        try:
            user_by_email = User.objects.get(email=username_or_email)
            user = authenticate(username=user_by_email.username, password=password)
        except User.DoesNotExist:
            user = None

    if user is not None:
        if user.is_active:
            # AQUÍ ES DONDE GENERAS TUS TOKENS (Asegúrate de usar tu lógica JWT)
            # Ejemplo simplificado, asegúrate de retornar 'role'
            from rest_framework_simplejwt.tokens import RefreshToken
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'role': user.role  # <--- ESTO ES LO QUE EL FRONTEND ESPERA
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Cuenta desactivada"}, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response({"error": "Usuario o contraseña incorrectos"}, status=status.HTTP_401_UNAUTHORIZED)

# --- RECUPERACIÓN ---
@api_view(['POST'])
def solicitar_recuperacion(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "No existe el usuario."}, status=status.HTTP_404_NOT_FOUND)

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    frontend_url = f"http://localhost:3000/recuperar-password?uid={uid}&token={token}"

    send_mail(
        "Recuperación de contraseña",
        f"Hola, haz clic aquí: {frontend_url}",
        "admin@alcaldiacucuta.gov.co",
        [user.email],
        fail_silently=False,
    )
    return Response({"mensaje": "Enlace enviado."}, status=status.HTTP_200_OK)

@api_view(['POST'])
def confirmar_recuperacion(request):
    uidb64 = request.data.get('uid')
    token = request.data.get('token')
    nueva_password = request.data.get('password')

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        return Response({"error": "Enlace inválido."}, status=status.HTTP_400_BAD_REQUEST)

    if default_token_generator.check_token(user, token):
        user.set_password(nueva_password)
        user.save()
        return Response({"mensaje": "Contraseña actualizada."}, status=status.HTTP_200_OK)
    return Response({"error": "Token inválido."}, status=status.HTTP_400_BAD_REQUEST)