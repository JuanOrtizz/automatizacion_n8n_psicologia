import logging
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from drf_spectacular.utils import extend_schema
from project.throttles import LoginAnonRateThrottle, RegisterAnonRateThrottle
from .serializers import UserSerializer

class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    throttle_classes = [ScopedRateThrottle, RegisterAnonRateThrottle]
    throttle_scope = 'register'
    
    def get_permissions(self):
        if self.action == 'register':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @extend_schema(summary="Registrar usuario", description="Registra un nuevo usuario. Requiere email autorizado.", auth=[])
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=201)

    @extend_schema(summary="Obtener usuario actual", description="Obtiene los datos del usuario autenticado actual")
    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        return Response(UserSerializer(request.user).data)

    @extend_schema(summary="Cerrar sesión", description="Cierra la sesión del usuario (invalida el token JWT)")
    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            request.auth.blacklist()
        except (AttributeError, TypeError):
            pass
        except Exception as e:
            logging.warning(f"Logout error: {e}")
        return Response({'message': 'Sesión cerrada'})
