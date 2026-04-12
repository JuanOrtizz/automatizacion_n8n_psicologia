import re

from django.forms import Select
from django.utils import timezone

from django import forms

class SesionesForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'id' : 'id_nombre'
            }
        ),
        max_length=100
    )

    dia_preferido = forms.ChoiceField(
        choices=[
            ('', 'Selecciona un día'),
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
            ('Sábado', 'Sábado'),
            ('Domingo', 'Domingo'),
        ],
        widget = Select(attrs={'id': 'id_dia_preferido', 'class': 'form-control'}),
    )

    fecha_solicitud = forms.DateField(
        label='Fecha de Solicitud',
        initial=timezone.now().date(),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'type': 'date',
                'placeholder': ' ',
                'readonly': 'readonly',
                'id': 'id_fecha_solicitud'
            }
        ),
    )

    dia_sesion = forms.ChoiceField(
        choices=[
            ('', 'Selecciona un día'),
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
            ('Sábado', 'Sábado'),
            ('Domingo', 'Domingo'),
        ],
        required=False,
        widget=Select(attrs={'id': 'id_dia_sesion', 'class': 'form-control'}),
    )

    horario_sesion = forms.TimeField(
        label='Horario de Sesión',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'time',
                'placeholder': ' ',
                'id': 'id_horario_sesion'
            }
        ),
    )

    telefono = forms.CharField(
        label='Teléfono',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'id': 'id_telefono'
            }
        ),
        max_length=25
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) >= 2 and len(nombre) <= 100:
            if not re.fullmatch(r'^[a-zA-ZáéíóúñÁÉÍÓÚÑ]+(?:\s[a-zA-ZáéíóúñÁÉÍÓÚÑ]+)*$', nombre, re.IGNORECASE):
                raise forms.ValidationError("El nombre no es válido (solo letras y espacios).")
        else:
            raise forms.ValidationError("Nombre: de 2 a 100 caracteres")
        return nombre

    def clean_dia_preferido(self):
        dia_preferido = self.cleaned_data.get('dia_preferido', '').title()
        if not dia_preferido:
            raise forms.ValidationError("El día preferido es obligatorio.")
        else:
            dias_validos = ['Lunes', 'Martes', 'Miércoles', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Sabado', 'Domingo']
            if dia_preferido not in dias_validos:
                raise forms.ValidationError("Día no válido")
        return dia_preferido

    def clean_fecha_solicitud(self):
        fecha_solicitud = self.cleaned_data.get('fecha_solicitud')
        if fecha_solicitud is None:
            raise forms.ValidationError("La fecha de solicitud es obligatoria.")
        return fecha_solicitud

    def clean_dia_sesion(self):
        dia_sesion = self.cleaned_data.get('dia_sesion', '').title()
        if dia_sesion:
            dias_validos = ['Lunes', 'Martes', 'Miércoles', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Sabado', 'Domingo']
            if dia_sesion not in dias_validos:
                raise forms.ValidationError("Día no válido")
        return dia_sesion

    def clean_horario_sesion(self):
        return self.cleaned_data.get('horario_sesion')

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono', '').strip()
        if len(telefono) >= 6 and len(telefono) <= 25:
            if not re.fullmatch(r'^\+?[0-9\s-]{6,25}$', telefono):
                raise forms.ValidationError("El teléfono no es válido.")
        else:
            raise forms.ValidationError("Teléfono: de 6 a 25 caracteres.")
        return telefono