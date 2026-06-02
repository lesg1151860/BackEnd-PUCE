from django.contrib import admin
from .models import InstitucionEducativa

@admin.register(InstitucionEducativa)
class InstitucionEducativaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'sector',)
    search_fields = ('nombre',)
    list_filter = ('sector',)