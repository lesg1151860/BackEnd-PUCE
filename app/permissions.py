from rest_framework.permissions import BasePermission


class IsAdminRole(BasePermission):
    message = 'Solo un administrador puede gestionar usuarios.'

    def has_permission(self, request, view):
        user = getattr(request, 'user', None)
        return bool(user and user.is_authenticated and getattr(user, 'role', None) == 'admin')
