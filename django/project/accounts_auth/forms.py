from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UsuariosAutorizados


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'id': 'id_username'
            }
        ),
        max_length=150
    )
    
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'id': 'id_email'
            }
        ),
        required=True
    )
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'id': 'id_password1'
            }
        ),
    )
    
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'id': 'id_password2'
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if not UsuariosAutorizados.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email no autorizado")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email ya registrado")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
