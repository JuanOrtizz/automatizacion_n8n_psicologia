from rest_framework import serializers
from django.contrib.auth.models import User
from ...models import UsuariosAutorizados

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined', 'is_active']
        read_only_fields = ['id', 'date_joined', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, attrs):
        email = attrs.get('email', '').lower()
        if not UsuariosAutorizados.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Email no autorizado")
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Email ya registrado")
        return attrs