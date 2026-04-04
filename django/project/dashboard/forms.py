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
            if not re.match(r'^[a-záéíóúñ]+(?:\s[a-záéíóúñ]+)*$', nombre, re.IGNORECASE):
                raise forms.ValidationError("El nombre no es válido (solo letras y espacios).")
        else:
            raise forms.ValidationError("Nombre: de 2 a 100 caracteres")
        return nombre

    def clean_dia_preferido(self):
        dia_preferido = self.cleaned_data.get('dia_preferido', '')
        if not dia_preferido:
            raise forms.ValidationError("El día preferido es obligatorio.")
        return dia_preferido

    def clean_fecha_solicitud(self):
        fecha_solicitud = self.cleaned_data.get('fecha_solicitud')
        if fecha_solicitud is None:
            raise forms.ValidationError("La fecha de solicitud es obligatoria.")
        return fecha_solicitud

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono', '').strip()
        if len(telefono) >= 6 and len(telefono) <= 25:
            if not re.match(r'^\+?[0-9]{6,25}$', telefono):
                raise forms.ValidationError("El teléfono no es válido.")
        else:
            raise forms.ValidationError("Teléfono: de 6 a 25 caracteres.")
        return telefono