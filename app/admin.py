from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Mostramos el método personalizado 'mostrar_grupos' en la tabla
    list_display = ('username', 'full_name', 'email', 'is_staff', 'is_active', 'mostrar_grupos')
    
    # Permitimos filtrar lateralmente por los grupos existentes
    list_filter = ('groups', 'is_staff', 'is_active')
    search_fields = ('username', 'full_name', 'email')
    ordering = ('full_name',)

    # UserAdmin ya maneja la edición de grupos por defecto, 
    # solo añadimos el campo de nombre completo a los bloques existentes.
    fieldsets = UserAdmin.fieldsets + (
        ('Información Personalizada', {
            'fields': ('full_name',),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Obligatoria', {
            'classes': ('wide',),
            'fields': ('full_name', 'email'),
        }),
    )

    # Función para renderizar los nombres de los grupos en la lista de usuarios
    def mostrar_grupos(self, obj):
        return ", ".join([grupo.name for grupo in obj.groups.all()])
    mostrar_grupos.short_description = 'Grupos / Roles'