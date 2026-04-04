from .models import Sesiones

def register_sesion(data):
    # capturo los datos del formulario
    nombre = data.get('nombre').strip()
    dia_preferido = data.get('dia_preferido')
    fecha_solicitud = data.get('fecha_solicitud')
    telefono = data.get('telefono').strip()

    # verifico si ya existe una sesión para ese cliente (nombre + teléfono)
    if Sesiones.objects.filter(nombre__iexact = nombre, telefono = telefono).exists():
        raise ValueError("Ya existe una sesión para ese cliente")

    # creo la nueva sesion y la guardo en la base de datos
    nueva_sesion = Sesiones(
        nombre=nombre,
        dia_preferido=dia_preferido,
        fecha_solicitud=fecha_solicitud,
        telefono=telefono
    )
    nueva_sesion.save()

    return nueva_sesion

def get_sesion(sesion_id):
    sesion = Sesiones.objects.get(id=sesion_id)
    return sesion

def get_sesions():
    sesiones = Sesiones.objects.all()
    return sesiones

def update_sesion(sesion, data):

    #Guardo los datos actuales para comparar después
    nombre_actual = sesion.nombre
    dia_preferido_actual = sesion.dia_preferido
    telefono_actual = sesion.telefono

    # capturo los datos del formulario
    nombre = data.get('nombre').strip()
    dia_preferido = data.get('dia_preferido')
    fecha_solicitud = data.get('fecha_solicitud')
    telefono = data.get('telefono').strip()

    if nombre == nombre_actual and dia_preferido_actual == dia_preferido and telefono == telefono_actual:
        raise ValueError("No realizaste modificaciones.")

    # verifico si ya existe una sesión para ese cliente (nombre + teléfono)
    if Sesiones.objects.filter(nombre__iexact = nombre, telefono = telefono).exclude(id=sesion.id).exists():
        raise ValueError("Ya existe una sesión para ese cliente")

    # actualizo los campos de la sesión
    sesion.nombre = nombre
    sesion.dia_preferido = dia_preferido
    sesion.telefono = telefono

    sesion.save()

    return sesion

def delete_sesion(sesion_id):
    # busco la sesión por su ID
    sesion = Sesiones.objects.get(id=sesion_id)
    if sesion:
        # elimino la sesión de la base de datos
        sesion.delete()
    else:
        raise ValueError("La sesión no existe")