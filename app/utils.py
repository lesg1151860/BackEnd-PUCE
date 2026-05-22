from django.core.exceptions import PermissionDenied
from functools import wraps

def admin_role_required(view_func):
    """
    Decorador personalizado para verificar si el usuario autenticado 
    tiene explícitamente el rol de 'admin'.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # 1. Verificar si el usuario inició sesión
        if not request.user.is_authenticated:
            raise PermissionDenied
        
        # 2. Verificar si el campo 'role' es 'admin'
        if request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        
        # Si no es admin, denegar el acceso inmediatamente
        raise PermissionDenied
        
    return _wrapped_view