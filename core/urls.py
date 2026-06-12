from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('accounts.urls')), # <-- Nueva ruta para registro
    path('api/', include('institucion_educativa.urls')), # Ruta para instituciones educativas
    path('api/', include('catalogos.urls')), # Ruta para catálogos
    path('api/', include('siuce.urls')), # Ruta para casos SIUCE
]