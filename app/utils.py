from django.core.exceptions import PermissionDenied
from functools import wraps

def grupo_requerido(nombre_grupo):
    """
    Decorador para restringir el acceso a vistas basado en grupos de Django.
    Permite el acceso si el usuario pertenece al grupo o si es un superusuario.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied
            
            # El superusuario de Django tiene acceso total por defecto
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
                
            # Verificar si el usuario pertenece al grupo solicitado
            if request.user.groups.filter(name=nombre_grupo).exists():
                return view_func(request, *args, **kwargs)
                
            raise PermissionDenied
        return _wrapped_view
    return decorator