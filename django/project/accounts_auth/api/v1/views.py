import logging
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
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

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=201)

    @action(detail=False, methods=['get'], url_path='me')
    def me(self, request):
        return Response(UserSerializer(request.user).data)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            request.auth.blacklist()
        except (AttributeError, TypeError):  # Error esperado
            pass
        except Exception as e:  # Error inesperado
            logging.warning(f"Logout error: {e}")
        return Response({'message': 'Sesión cerrada'})
