from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('catalogos.urls')), # Ruta para catálogos
    path('api/', include('siuce.urls')), # Ruta para casos SIUCE
]