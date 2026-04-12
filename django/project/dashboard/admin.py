from django.contrib import admin
from .models import Sesiones

@admin.register(Sesiones)
class SesionesAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'telefono', 'fecha_solicitud', 'dia_sesion', 'horario_sesion']
    readonly_fields = ['fecha_solicitud']