from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Controla las columnas que se muestran en la tabla principal de usuarios
    list_display = ('username', 'full_name', 'email', 'role', 'is_staff', 'is_active')
    
    # Añade filtros laterales para buscar usuarios rápidamente por rol o estado
    list_filter = ('role', 'is_staff', 'is_active')
    
    # Permite buscar usuarios por nombre completo, usuario o correo
    search_fields = ('username', 'full_name', 'email')
    
    # Orden predeterminado por nombre completo
    ordering = ('full_name',)

    # Modifica los formularios de edición para incluir tus campos personalizados
    fieldsets = UserAdmin.fieldsets + (
        ('Información de Roles del Sistema', {
            'fields': ('full_name', 'role'),
        }),
    )

    # Modifica el formulario de creación de usuario para incluir los campos obligatorios
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Obligatoria', {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'role'),
        }),
    )