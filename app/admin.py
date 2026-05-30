from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 1. Agregamos 'date_joined' a la lista para verlo en la tabla principal
    list_display = ('username', 'full_name', 'email', 'role', 'is_active', 'mostrar_grupos', 'date_joined')
    
    list_filter = ('groups', 'role', 'is_active', 'date_joined') # Filtro por fecha opcional
    search_fields = ('username', 'full_name', 'email', 'role')
    ordering = ('-date_joined',) # Ordenamos por los más recientes primero

    # 2. 'date_joined' y 'last_login' son automáticos y no deben ser editables
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ('groups',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {
            'fields': ('full_name', 'email', 'role')
        }),
        ('Permisos', {
            'fields': ('is_active',), 
        }),
        ('Grupos y Roles', {
            'fields': ('groups',),
        }),
        ('Fechas de Control', {
            'fields': ('date_joined', 'last_login'), # Visualización de fecha de creación
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Obligatoria', {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'role'),
        }),
    )

    def mostrar_grupos(self, obj):
        return ", ".join([grupo.name for grupo in obj.groups.all()])
    mostrar_grupos.short_description = 'Grupos / Roles'