from django.db import models

class Sesiones(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    dia_preferido = models.CharField(max_length=20)
    fecha_solicitud = models.DateField(auto_now_add=True, db_index=True)
    dia_sesion = models.CharField(null=True, blank=True)
    horario_sesion = models.TimeField(null=True, blank=True)
    telefono = models.CharField(max_length=25)

    class Meta:
        db_table = 'sesiones'
        constraints = [
            models.UniqueConstraint(
                fields=['nombre', 'telefono', 'dia_sesion'],
                name='unique_sesion_cliente'
            )
        ]