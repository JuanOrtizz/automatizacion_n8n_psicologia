import re

from rest_framework import serializers
from ...models import Sesiones

class SesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesiones
        fields = ['id', 'nombre', 'dia_preferido', 'fecha_solicitud', 'dia_sesion', 'horario_sesion', 'telefono']
        read_only_fields = ['fecha_solicitud']

    def validate_nombre(self, value):
        value = value.strip().title()
        if len(value) < 2 or len(value) > 100:
            raise serializers.ValidationError("Nombre: de 2 a 100 caracteres")
        if not re.fullmatch(r'^[a-zA-ZáéíóúñÁÉÍÓÚÑ]+(?:\s[a-zA-ZáéíóúñÁÉÍÓÚÑ]+)*$', value, re.IGNORECASE):
            raise serializers.ValidationError("El nombre no es válido (solo letras y espacios)")
        return value

    def validate_dia_preferido(self, value):
        value = value.strip().title()
        if not value:
            raise serializers.ValidationError("El día preferido es obligatorio")
        dias_validos = ['Lunes', 'Martes', 'Miércoles', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Sabado', 'Domingo']
        if value not in dias_validos:
            raise serializers.ValidationError("Día no válido")
        return value

    def validate_dia_sesion(self, value):
        if value is None:
            return value
        value = value.strip().title()
        if value:
            dias_validos = ['Lunes', 'Martes', 'Miércoles', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Sabado', 'Domingo']
            if value not in dias_validos:
                raise serializers.ValidationError("Día no válido")
        return value

    def validate_horario_sesion(self, value):
        return value

    def validate_telefono(self, value):
        value = value.strip()
        if len(value) < 6 or len(value) > 25:
            raise serializers.ValidationError("Teléfono: de 6 a 25 caracteres")
        if not re.fullmatch(r'^\+?[0-9\s-]{6,25}$', value):
            raise serializers.ValidationError("El teléfono no es válido")
        return value
