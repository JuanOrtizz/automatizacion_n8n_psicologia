from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema
from ...models import Sesiones
from .serializers import SesionesSerializer

@extend_schema(tags=['dashboard'])
class SesionesViewSet(viewsets.ModelViewSet):
    queryset = Sesiones.objects.all()
    serializer_class = SesionesSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @extend_schema(summary="Listar sesiones", description="Obtiene todas las sesiones del usuario autenticado")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(summary="Crear sesión", description="Registra una nueva sesión")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(summary="Obtener sesión", description="Obtiene una sesión por ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(summary="Actualizar sesión", description="Actualiza una sesión por ID")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(summary="Eliminar sesión", description="Elimina una sesión por ID")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
