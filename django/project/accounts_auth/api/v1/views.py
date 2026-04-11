from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    
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
    
    @action(detail=False, methods=['patch'])
    def update_me(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @action(detail=False, methods=['delete'])
    def delete_me(self, request):
        request.user.delete()
        return Response(status=204)
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            request.auth.blacklist()
        except:
            pass
        return Response({'message': 'Sesión cerrada'})
