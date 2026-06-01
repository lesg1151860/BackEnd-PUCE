from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include('accounts.urls')),  # Agrega esta línea para incluir las URLs de accounts
]
    