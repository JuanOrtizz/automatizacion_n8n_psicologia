from .models import Sesiones

def register_session(data):
    # capturo los datos del formulario
    nombre = data.get('nombre').strip().title()
    dia_preferido = data.get('dia_preferido')
    fecha_solicitud = data.get('fecha_solicitud')
    dia_sesion = data.get('dia_sesion')
    horario_sesion = data.get('horario_sesion')
    telefono = data.get('telefono').strip()

    if dia_sesion == '':
        dia_sesion = None

    # verifico si ya existe una sesión para ese cliente (nombre + teléfono + dia de sesión)
    if not dia_sesion is None:
        if Sesiones.objects.filter(nombre__iexact = nombre, telefono = telefono, dia_sesion = dia_sesion).exists():
            raise ValueError(f'Ya existe una sesión para el cliente {nombre} con el teléfono {telefono} para el día {dia_sesion}')

    # creo la nueva sesion y la guardo en la base de datos
    nueva_sesion = Sesiones(
        nombre=nombre,
        dia_preferido=dia_preferido,
        fecha_solicitud=fecha_solicitud,
        dia_sesion=dia_sesion,
        horario_sesion=horario_sesion,
        telefono=telefono
    )
    nueva_sesion.save()

    return nueva_sesion

def get_session(sesion_id):
    try:
        return Sesiones.objects.get(id=sesion_id)
    except Sesiones.DoesNotExist:
        raise ValueError("Sesión no encontrada")

def get_sessions():
    sesiones = Sesiones.objects.all()
    return sesiones

def update_session(sesion, data):

    #Guardo los datos actuales para comparar después
    nombre_actual = sesion.nombre
    dia_preferido_actual = sesion.dia_preferido
    dia_sesion_actual = sesion.dia_sesion
    horario_sesion_actual = sesion.horario_sesion
    telefono_actual = sesion.telefono

    # capturo los datos del formulario
    nombre = data.get('nombre').strip().title()
    dia_preferido = data.get('dia_preferido')
    dia_sesion = data.get('dia_sesion')
    horario_sesion = data.get('horario_sesion')
    telefono = data.get('telefono').strip()

    if dia_sesion == '':
        dia_sesion = None

    if dia_sesion_actual == '':
        dia_sesion_actual = None

    if nombre == nombre_actual and dia_preferido_actual == dia_preferido and telefono == telefono_actual and dia_sesion == dia_sesion_actual and horario_sesion == horario_sesion_actual:
        raise ValueError("No realizaste modificaciones.")

    # verifico si ya existe una sesión para ese cliente (nombre + teléfono + dia de sesión)
    if not dia_sesion is None:
        if Sesiones.objects.filter(nombre__iexact = nombre, telefono = telefono, dia_sesion = dia_sesion).exists():
            raise ValueError(f'Ya existe una sesión para el cliente {nombre} con el teléfono {telefono} para el día {dia_sesion}')

    # actualizo los campos de la sesión
    sesion.nombre = nombre
    sesion.dia_preferido = dia_preferido
    sesion.dia_sesion = dia_sesion
    sesion.horario_sesion = horario_sesion
    sesion.telefono = telefono

    sesion.save()

    return sesion

def delete_session(sesion_id):
    try:
        Sesiones.objects.get(id=sesion_id).delete()
    except Sesiones.DoesNotExist:
        raise ValueError("Sesión no encontrada")