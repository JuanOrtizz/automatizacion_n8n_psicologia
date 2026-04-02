from django.db import models

class Sesiones(models.Model):
    nombre = models.CharField(max_length=100)
    dia_preferido = models.CharField(max_length=20)
    fecha_solicitud = models.DateField(auto_now_add=True)
    telefono = models.CharField(max_length=25)

    class Meta:
        db_table = 'sesiones'