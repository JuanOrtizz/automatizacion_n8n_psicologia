from django.db import models

# Create your models here.
class UsuariosAutorizados(models.Model):
    email = models.EmailField(unique=True, db_index=True)
    fecha_autorizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuarios_autorizados'