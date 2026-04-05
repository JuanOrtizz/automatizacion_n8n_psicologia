from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from .forms import SesionesForm
from .services import register_sesion, get_sesion, get_sesions, update_sesion, delete_sesion

@login_required
def dashboard(request):
    filter = request.GET.get('filter', '')
    sesions = get_sesions()
    match filter:
        case "1": #Dia de hoy
            sesions = sesions.filter(fecha_solicitud = now().date())
        case "2": # Mas antiguas
            sesions = sesions.order_by('fecha_solicitud')
        case "3": # Mas recientes
            sesions = sesions.order_by('-fecha_solicitud')

    return render(request, 'dashboard/index.html', {'sesions': sesions, 'filter' : filter})

@login_required
def registrar_sesion(request):
    titulo_form = "Registrar Sesión"
    if request.method == 'POST':
        form = SesionesForm(request.POST)
        if form.is_valid():
            try:
                register_sesion(form.cleaned_data)
                return JsonResponse({'success': True, 'message': 'Sesión registrada con éxito'})
            except ValueError as e:
                return JsonResponse({'success': False, 'errors': str(e)})
        else:
            return JsonResponse({'success': False, 'message': 'Datos inválidos', 'errors': form.errors})
    else:
        form = SesionesForm()
    return render(request, 'dashboard/create_update_sesion.html', {'form': form, 'titulo_form': titulo_form})

@login_required
def modificar_sesion(request, sesion_id):
    titulo_form = "Modificar Sesión"
    sesion = get_sesion(sesion_id)
    if request.method == 'POST':
        form = SesionesForm(request.POST)
        if form.is_valid():
            try:
                update_sesion(sesion, form.cleaned_data)
                return JsonResponse({'success': True, 'message': 'Sesión modificada con éxito'})
            except ValueError as e:
                return JsonResponse({'success': False, 'errors': str(e)})
    else:
        form = SesionesForm(initial={
            'nombre': sesion.nombre,
            'dia_preferido': sesion.dia_preferido,
            'fecha_solicitud': sesion.fecha_solicitud,
            'telefono': sesion.telefono
        })

    return render(request, 'dashboard/create_update_sesion.html', {'form': form, 'titulo_form': titulo_form, 'sesion_id': sesion_id})

@login_required()
def eliminar_sesion(request, sesion_id):
    if request.method == 'POST':
        try:
            delete_sesion(sesion_id)
            return JsonResponse({'success': True, 'message': 'Sesión eliminada con éxito'})
        except ValueError as e:
            return JsonResponse({'success': False, 'errors': str(e)})