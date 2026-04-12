from rest_framework import serializers
from django.contrib.auth.models import User
from ...models import UsuariosAutorizados

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined', 'is_active']
        read_only_fields = ['id', 'date_joined', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        email = value.lower() if value else ''
        if not UsuariosAutorizados.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Email no autorizado")
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Email ya registrado")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user