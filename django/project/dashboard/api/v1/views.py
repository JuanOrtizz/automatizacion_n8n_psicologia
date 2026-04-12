from rest_framework import viewsets, permissions
from ...models import Sesiones
from .serializers import SesionesSerializer

class SesionesViewSet(viewsets.ModelViewSet):
    queryset = Sesiones.objects.all()
    serializer_class = SesionesSerializer
    permission_classes = [permissions.IsAuthenticated]
