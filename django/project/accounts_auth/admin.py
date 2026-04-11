from django.contrib import admin
from .models import UsuariosAutorizados

@admin.register(UsuariosAutorizados)
class UsuariosAutorizadosAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'fecha_autorizacion']
    readonly_fields = ['fecha_autorizacion']