from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from .forms import SesionesForm
from .services import register_session, get_session, get_sessions, update_session, delete_session

@login_required
def dashboard(request):
    filter_fecha_registro = request .GET.get('filter_fecha_registro', '')
    filter_dia_sesion = request.GET.get('filter_dia_sesion', '')

    if filter_dia_sesion == "":
        sessions = get_sessions()
    else:
        sessions = get_sessions().filter(dia_sesion=filter_dia_sesion)

    match filter_fecha_registro:
        case "1": #Dia de hoy
            sessions = sessions.filter(fecha_solicitud = now().date())
        case "2": # Mas antiguas
            sessions = sessions.order_by('fecha_solicitud')
        case "3": # Mas recientes
            sessions = sessions.order_by('-fecha_solicitud')

    return render(request, 'dashboard/index.html', {'sessions': sessions, 'filter_fecha_registro': filter_fecha_registro,'filter_dia_sesion' : filter_dia_sesion})

@login_required
def registrar_sesion(request):
    titulo_form = "Registrar Sesión"
    if request.method == 'POST':
        form = SesionesForm(request.POST)
        if form.is_valid():
            try:
                register_session(form.cleaned_data)
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
    sesion = get_session(sesion_id)
    if request.method == 'POST':
        form = SesionesForm(request.POST)
        if form.is_valid():
            try:
                update_session(sesion, form.cleaned_data)
                return JsonResponse({'success': True, 'message': 'Sesión modificada con éxito'})
            except ValueError as e:
                return JsonResponse({'success': False, 'errors': str(e)})
    else:
        form = SesionesForm(initial={
            'nombre': sesion.nombre,
            'dia_preferido': sesion.dia_preferido,
            'fecha_solicitud': sesion.fecha_solicitud,
            'dia_sesion': sesion.dia_sesion,
            'horario_sesion': sesion.horario_sesion,
            'telefono': sesion.telefono
        })

    return render(request, 'dashboard/create_update_sesion.html', {'form': form, 'titulo_form': titulo_form, 'sesion_id': sesion_id})

@login_required()
def eliminar_sesion(request, sesion_id):
    if request.method == 'POST':
        try:
            delete_session(sesion_id)
            return JsonResponse({'success': True, 'message': 'Sesión eliminada con éxito'})
        except ValueError as e:
            return JsonResponse({'success': False, 'errors': str(e)})