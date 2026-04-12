# Sistema de Chatbots y Dashboard de gestión

## Descripción

**Sistema de Chatbots que incluye:**
- Chatbot de atención al cliente (**Instagram**).
- Chatbot terapéutico con IA (**WhatsApp**).
- **Dashboard web** para la gestión de sesiones psicológicas.

> Utiliza **n8n** para la automatización de flujos de conversación y **Django** como backend y panel de administración.

El proyecto Django funciona como **backend y panel de administración** del sistema, permitiendo la gestión de sesiones psicológicas mediante un dashboard web y API REST con autenticación JWT.

---

## Diagrama de Flujo del Proyecto

> [Diagrama de flujo](https://excalidraw.com/#json=QO_P94ZifjeQv-pqLbBe1,7PE0po91e8gi6y1Jhg5TPg)

>[!TIP] 
>Se recomienda abrir el diagrama en una nueva pestaña para una mejor visualización.

## Arquitectura

**MVT (Model-View-Template)** - Patrón de arquitectura de Django

- **Model**: Modelos Django (Sesiones, UsuariosAutorizados)
- **View**: Vistas Django + Viewsets DRF
- **Template**: Templates HTML con Bootstrap + JavaScript

---

## Tecnologías

- **Django**: Framework web para el backend y panel de administración
- **Django REST Framework**: API REST para consumo externo
- **JWT (djangorestframework-simplejwt)**: Autenticación mediante tokens
- **PostgreSQL**: Base de datos relacional
- **WhiteNoise**: Staticfiles comprimidos para producción
- **Bootstrap 5**: Frontend responsive
- **SweetAlert2**: Notificaciones interactivas
- **n8n**: Plataforma de automatización para chatbots
- **Docker**: Contenerización de la aplicación
- **Docker Compose**: Orquestación de servicios

---

## Autenticación

El sistema utiliza un esquema de autenticación dual:

### Django Auth (Sesiones web)
- Utilizado para el acceso al dashboard web
- Decorador `@login_required` en todas las vistas

### JWT (API REST)
- **Access Token**: 30 minutos de duración
- **Refresh Token**: 1 día de duración con rotación automática
- **Blacklist**: Los tokens refresh se bloquean después de ser rotados
- Utilizado para consumo externo de la API REST

### Rate Limiting
Protección contra ataques de fuerza bruta mediante limitación de requests.

| Endpoint | Límite | Descripción |
|----------|--------|-------------|
| `/api/v1/users/register/` | 5/hour | Máximo 5 registros por hora por IP |
| `/api/v1/auth/token/` | 5/minute | Máximo 5 intentos de login por minuto |
| `/api/v1/auth/token/refresh/` | 5/minute | Máximo 5 refresh por minuto |
| Global (anónimo) | 100/day | Máximo 100 requests/día |

---

## Modelos

### Sesiones
Modelo para la gestión de sesiones psicológicas.

| Campo | Tipo | Descripción                       |
|-------|------|-----------------------------------|
| nombre | CharField(100) | Nombre del paciente               |
| dia_preferido | CharField(20) | Día preferido por el paciente     |
| fecha_solicitud | DateField | Fecha de registro (auto_now_add)  |
| dia_sesion | CharField(null=True) | Día específico de la sesión       |
| horario_sesion | TimeField(null=True) | Horario de la sesión              |
| telefono | CharField(25) | Teléfono de contacto del paciente |

**Características adicionales:**
- Índices de optimización en `nombre` y `fecha_solicitud`
- Restricción única: nombre + teléfono + día de sesión

### UsuariosAutorizados
Modelo para whitelist de seguridad de emails autorizados.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| email | EmailField | Email autorizado (unique) |
| fecha_autorizacion | DateTimeField | Fecha de autorización (auto_now_add) |

---

## Funcionalidades Principales

### Dashboard

#### Filtros de Sesiones
- **Por fecha de registro:**
  - Sesiones del día de hoy
  - Sesiones más antiguas
  - Sesiones más recientes
- **Por día de sesión:**
  - Filtrar por día específico (Lunes - Domingo)

#### Gestión de Sesiones
- Registro de nuevas sesiones
- Modificación de sesiones existentes
- Eliminación de sesiones con confirmación
- Validaciones client-side y server-side

#### Panel de Administración Django
- Modelos registrados: Sesiones, UsuariosAutorizados
- Visualización y gestión de datos

### Autenticación

#### Registro de Usuarios
- Formulario web de registro
- Endpoint API para registro externo
- Validación de email contra lista de usuarios autorizados
- Contraseña con validación Django

#### Gestión de Sesiones
- Login/Logout web tradicional
- Logout con blacklist de tokens JWT
- Protección de vistas con decorador @login_required

### API REST v1

#### Endpoints de Sesiones (dashboard)
```
GET    /api/v1/sesiones/          # Listar todas las sesiones
POST   /api/v1/sesiones/          # Crear nueva sesión
GET    /api/v1/sesiones/{id}/     # Obtener sesión específica
PUT    /api/v1/sesiones/{id}/     # Actualizar sesión
DELETE /api/v1/sesiones/{id}/     # Eliminar sesión
```

#### Endpoints de Usuarios (accounts_auth)
```
POST   /api/v1/users/register/    # Registro de nuevo usuario
GET    /api/v1/users/me/          # Obtener perfil del usuario autenticado
POST   /api/v1/users/logout/      # Cerrar sesión (blacklist de token)
```

#### Endpoints de Autenticación JWT
```
POST   /api/v1/auth/token/        # Obtener access token (login API)
POST   /api/v1/auth/token/refresh/  # Refrescar access token
```

---

## Requisitos Previos

- [Docker](https://www.docker.com/) y Docker Compose

---

## Instalación y Ejecución

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd <path-del-repo>

# Levantar los servicios (instala dependencias, ejecuta migraciones y arranca automáticamente)
docker-compose up --build
```

Servicios disponibles:
- **Django**: http://localhost:8000
- **n8n**: http://localhost:5678

---

## Estructura del Proyecto

```
automatizacion_n8n_psicologia/
├── django/
│   └── project/
│       ├── dashboard/         # App de gestión de sesiones
│       ├── accounts_auth/     # App de autenticación
│       ├── project/           # Configuración del proyecto
│       └── manage.py
├── n8n/
├── CHANGELOG.md
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Notas

- Los flujos de n8n se almacenan en el volumen `n8n_data`.
- Se puede usar un archivo `docker-compose.override.yml` para configurar un volumen externo para persistir los datos de n8n en caso de necesitarlo.

---

## Versión

**v1.0.0**