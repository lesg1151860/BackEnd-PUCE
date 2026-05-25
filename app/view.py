# app/views.py
import email

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from .models import User

@api_view(['POST'])
def solicitar_recuperacion(request):
    email = request.data.get('email')
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Cambio aplicado: Retorna 404 si no encuentra el correo
        return Response(
            {"error": "No existe ningún usuario registrado con este correo."}, 
            status=status.HTTP_404_NOT_FOUND
        )

    # Si pasa el except, significa que el correo SÍ existe y continúa el proceso
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    frontend_url = f"http://localhost:3000/recuperar-password?uid={uid}&token={token}"

    send_mail(
        subject="Recuperación de contraseña - Sistema de Convivencia",
        message=f"Hola {user.full_name},\n\nHaz clic en el siguiente enlace para restablecer tu contraseña:\n{frontend_url}\n\nSi no solicitaste este cambio, ignora este mensaje.",
        from_email="admin@alcaldiacucuta.gov.co",
        recipient_list=[user.email],
        fail_silently=False,
    )

    return Response({"mensaje": "Se ha enviado un enlace de recuperación a tu correo."}, status=status.HTTP_200_OK)


@api_view(['POST'])
def confirmar_recuperacion(request):
    uidb64 = request.data.get('uid')
    token = request.data.get('token')
    nueva_password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Opción: Priorizar UX informando al usuario que se equivocó al digitar
        return Response(
            {"error": "No existe ningún usuario registrado con este correo."}, 
            status=status.HTTP_404_NOT_FOUND
        )