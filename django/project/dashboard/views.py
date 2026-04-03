from django.http import JsonResponse
from django.shortcuts import render
from .forms import SesionesForm
from .models import Sesiones

def dashboard(request):
    sesiones = Sesiones.objects.all()
    #Agregar filtros
    return render(request, 'dashboard/index.html', {'sesiones': sesiones})

def registrar_sesion(request):
    if request.method == 'POST':
        form = SesionesForm(request.POST)
        if form.is_valid():
            # capturo los datos del formulario
            nombre = form.cleaned_data['nombre'].strip()
            dia_preferido = form.cleaned_data['dia_preferido']
            fecha_solicitud = form.cleaned_data['fecha_solicitud']
            telefono = form.cleaned_data['telefono'].strip()

            # verifico si ya existe una sesión para ese cliente (nombre + teléfono)
            if Sesiones.objects.filter(nombre = nombre, telefono = telefono).exists():
                return JsonResponse({'success': False, 'errors': 'Ya existe una sesión para ese cliente'})

            # creo la nueva sesion y la guardo en la base de datos
            nueva_sesion = Sesiones(
                nombre=nombre,
                dia_preferido=dia_preferido,
                fecha_solicitud=fecha_solicitud,
                telefono=telefono
            )
            nueva_sesion.save()
            return JsonResponse({'success': True, 'message': 'Sesión registrada con éxito.'})
        else:
            return JsonResponse({'success': False, 'message': 'Datos inválidos', 'errors': form.errors})
    else:
        form = SesionesForm()
    return render(request, 'dashboard/register_sesion.html', {'form': form})