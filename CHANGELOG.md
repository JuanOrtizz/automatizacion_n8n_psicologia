# Changelog
---
## [v1.1.0] - 2026-04-22
### Rama: release/v1.1.0

#### Docs
- Actualización de CHANGELOG.md
- Actualización de README.md

## [v1.1.0] - 2026-04-22
### Rama: feature/docs-api
#### Features
- Agregado de drf-spectacular para documentación de API REST
- Agregadas rutas `/api/docs/` (Swagger UI) y `/api/schema/` (OpenAPI 3.0)
- Agregada documentación de endpoints en views (SesionesViewSet, UserViewSet, Token endpoints)

#### Docs
- Documentación de todos los endpoints de la API:
  - Sesiones: list, create, retrieve, update, destroy
  - Users: register, me, logout
  - Token: obtain, refresh
---

## [v1.0.2] - 2026-04-14
### Rama: hotfix/modificar-sesion
#### Fixes
- Corrección de bug de modificación de sesión

---

## [v1.0.1] - 2026-04-13
### Rama: hotfix/debug-env-y-dockerfile-cmd
#### Features
- Agregado de creación de superusuario django en Dockerfile

#### Fixes
- Arreglo de cast de variable de entorno DEBUG a booleano en settings.py
---

## [v1.0.0] - 2026-04-12
### Rama: release/v1.0.0
#### Features
- Agregado de paquetes dj-database-url y python-decouple para configuración de variables de entorno
- Agregado de conexión a DB por URL (DATABASE_URL)
- Definición de ALLOWED_HOST en settings
- Agregado de variables de entorno en servicio n8n
- Agregado de servicio ngrok en docker-compose.yml
- Agregado de medidas de seguridad en el proyecto django (HTTPS/SSL, Headers de seguridad, Cookies seguras)

#### Fixes
- Agregado de variables de entorno en rate limit para que no este hardcodeado en settings.py

#### Docs
- Actualización de README.md
- Agregado de CHANGELOG.md
---

## [v1.0.0] - 2026-04-11
### Rama: feature/cambios-pre-release-v1.0.0
#### Features
- Registro de modelos Sesiones y UsuariosAutorizados en panel admin Django
- Agregado de nuevos campos de modelo Sesiones: dia_sesion, horario_sesion
- Agregado de índices para optimización en modelo Sesiones
- Agregado de migraciones de modelo Sesiones con nuevos campos
- Agregado de modelo UsuariosAutorizados para seguridad en app accounts_auth
- Agregado de migraciones de modelo UsuariosAutorizados
- Agregado de validaciones de email en RegistroForm en app accounts_auth
- Agregado de validaciones de email con autorización admin en UserSerializer
- Agregado de nuevo filtro (dia_sesion) en view dashboard
- Agregado de script js de filtros actualizado para nuevos campos
- Agregado de estilo para filtros de index (dashboard)
- Agregado de nuevos campos de modelo en template index.html (dashboard)
- Agregado de nuevos campos de modelo y validaciones en api/v1/serializers (dashboard)
- Agregado de nuevos campos de modelo en view modificar_sesion (dashboard)
- Agregado de nuevos campos de modelo y validaciones en forms (dashboard)
- Agregado de nuevos campos de modelo y validaciones en services (dashboard)
- Agregado de control de excepciones en endpoint logout
- Agregado de sistema de Rate Limiting para protección de endpoints de autenticación:
  - Throttle para registro: 5 requests/hora por IP
  - Throttle para login/token: 5 requests/minuto por IP
  - Throttle global para anónimos: 100 requests/día
- Añadido app de token blacklist para gestión de invalidate de tokens
- Corregido imports en accounts_auth API (throttles)
- Mejorado UserSerializer: email requerido, validación corregida y método create con hash de password
- Agregado campo no requerido en dia_sesion en SesionesSerializer
-  Agregado el completado de texto si hay valores None desde el backend en template index (dashboard)"

#### Fixes
- Corrección de error de name en llamadas a scripts js en template create_update_sesion
- Corrección de bug de regex en validación de input nombre en script js SessionValidations

#### Refactor
- Refactorización de código en template index (dashboard) para nuevo filtro
- Corrección de palabra "sesions" a "sessions" en archivos js
- Eliminación de endpoints `update_me` y `delete_me` en UserViewSet de API v1 (accounts_auth) para simplificación de la API
---

## [v1.0.0] - 2026-04-05
### Rama: feature/api-v1-accounts-auth
#### Features
- Instalación del paquete JWT (djangorestframework-simplejwt) para autenticación
- Agregado de estructura de directorios para API v1
- Agregado de UserSerializer para API v1 de accounts_auth con validaciones de creación
- Agregado de UserViewSet con endpoints personalizados:
  - `POST /api/v1/users/register/` - Registro de usuarios
  - `GET /api/v1/users/me/` - Obtener perfil del usuario autenticado
  - `PATCH /api/v1/users/update_me/` - Actualizar perfil del usuario
  - `DELETE /api/v1/users/delete_me/` - Eliminar cuenta de usuario
  - `POST /api/v1/users/logout/` - Cerrar sesión (blacklist de token)
- Agregado de rutas API v1 para tokens JWT (obtain y refresh)
- Agregado de configuración de JWT en settings:
  - Access token lifetime: 30 minutos
  - Refresh token lifetime: 1 día
  - Rotación de refresh tokens habilitada
  - Blacklist después de rotación

#### Fixes
- Corrección de Dockerfile añadiendo collectstatic al CMD
- Agregado de decorador @login_required en view eliminar_sesion para evitar vulnerabilidad de seguridad

#### Refactor
- Actualización de urls para incluir API v1 en app accounts_auth

---

## [v1.0.0] - 2026-04-05
### Rama: feature/auth
#### Features
- Creación de app accounts (auth) para gestión de usuarios
- Agregado de sistema de autenticación con Django Auth
- Agregado de urls de autenticación y solución de errores producidos por cambio de nombre de app accounts en settings.py
- Agregado de decorador 'login_required' en todas las views de app Dashboard
- Agregado de forms.py con form RegistroForm personalizado basado en UserCreationForm
- Agregado de views.py con SignUpView (CreateView) para registro de usuarios
- Agregado de urls.py con el enrutamiento de las rutas en app accounts_auth
- Agregado de templates login.html y registro.html para autenticación
- Configuración de LOGIN_URL, LOGIN_REDIRECT_URL y LOGOUT_REDIRECT_URL en settings

#### Refactor
- Cambio de nombre de app a 'accounts_auth'
- Cambio de nombre de template_name en view SignUpView (accounts_auth)
- Actualización de urls.py del proyecto con las urls de la nueva app accounts_auth
- Actualización de botón de logout para el correcto funcionamiento con django.auth

---

## [v1.0.0] - 2026-04-05
### Rama: feature/api-v1-sesiones
#### Features
- Agregado de estructura de directorios para API v1 (dashboard)
- Agregado de SesionesSerializer con validaciones para API REST:
  - Validación de nombre: 2-100 caracteres, solo letras y espacios
  - Validación de día preferido: obligatorio, debe ser un día válido
  - Validación de teléfono: 6-25 caracteres, solo números y opcionalmente +
- Agregado de SesionesViewSet con permisos IsAuthenticated (ModelViewSet completo)
- Agregado de router y URLs para api/v1/sesiones (CRUD completo)
- Registro de Django REST Framework en INSTALLED_APPS

#### Refactor
- Actualización de urls.py para incluir rutas de API v1 (dashboard)

---

## [v1.0.0] - 2026-04-04
### Rama: feature/app-dashboard
#### Features
- Agregado de Django REST Framework al proyecto y registrado en requirements.txt
- Actualización de filtros en template index (dashboard) para filtrar sesiones:
  - Filter 1: Sesiones del día de hoy
  - Filter 2: Sesiones más antiguas
  - Filter 3: Sesiones más recientes
- Agregado de filtros en la view Dashboard (implementación con match/case)
- Agregado de script (js) para los filtros de sesiones del dashboard
- Agregado de vistas Modificar_session, Eliminar_session y actualización de vistas registrar_session y dashboard
- Agregado de services.py con servicios CRUD del modelo Sesiones:
  - register_session - Registrar nueva sesión
  - get_session - Obtener sesión por ID
  - get_sessions - Obtener todas las sesiones
  - update_session - Actualizar sesión existente
  - delete_session - Eliminar sesión
- Agregado y actualización de nomenclaturas de rutas en urls.py de app dashboard
- Agregado de script .js para mostrar alerts de actualización de sesión exitosa en index(dashboard)
- Actualización de templates html de app dashboard
- Actualización de script .js para registrar una sesión
- Agregado de script .js para eliminar una sesión
- Agregado de script .js para actualizar una sesión
- Agregado de alerta de confirmación en alerts.js (SweetAlert2)
- Actualización de choices de select dia_preferido en form 'Sesiones'
- Agregado de vista registrar_sesion
- Actualización de register_sesion (Template) para el funcionamiento del registro
- Agregado de script para crear objeto Sesion con fetch
- Agregado de script para validar campos de modelo Sesiones en el front
- Actualización de campo 'dia_preferido' en form 'Sesiones'
- Agregado de script para alertas SweetAlerts2
- Agregado de vista y enrutamiento para 'register_sesion'
- Agregado de clases para los fields en formulario 'Sesiones'
- Agregado de template 'register_sesion.html'
- Agregado de logo de app en 'base.html'
- Agregado de logo de app (webp)
- Agregado de formulario de Sesiones (Registro y Modificación)
- Enruto de dashboard como ruta principal
- Agregado de conexión a DB PostgreSQL
- Agregado de modelo 'Sesiones' con campos: nombre, dia_preferido, fecha_solicitud, telefono
- Agregado de index.html (Dashboard) base
- Agregado de js 'index' de app 'Dashboard'
- Agregado de css 'Dashboard' de app 'Dashboard'
- Registro de urls de app 'dashboard' en 'urls.py' (Global)
- Registro de app 'dashboard' en 'settings.py'
- Creación de app 'dashboard'
- Agregado de static js (Global)
- Agregado de static css (Global)
- Agregado de templates base (base | header | footer)
- Integración de Bootstrap para estilos responsive
- Integración de SweetAlert2 para notificaciones interactivas
- Configuración de STATIC_ROOT con WhiteNoise para staticfiles comprimidos

#### Fixes
- Actualización de estilo de filtro y botón de registro de sesión en 'dashboard.html'

#### Refactor
- Eliminación de comentarios no necesarios en scripts (js) alerts y showSuccessMessage
- Uso de patrón match/case para implementación de filtros en views

#### Notas
- Migraciones de app Dashboard

---

## [v1.0.0] - 2026-04-03
### Rama: feature/setup
#### Features
- Agregado de proyecto Django inicializado (versión 6.0.3)
- Agregado de 'Dockerfile' para imagen Django
- Agregado de 'Docker-compose.yml' con servicios Django y PostgreSQL
- Agregado de .gitignore
- Agregado de README.md
- Configuración de idioma español argentino (LANGUAGE_CODE: es-ar)
- Configuración de zona horaria UTC

#### Notas
- Actualización de requirements.txt con paquetes:
  - asgiref==3.11.1
  - Django==6.0.3
  - djangorestframework==3.17.1
  - djangorestframework_simplejwt==5.5.1
  - gunicorn==25.3.0
  - packaging==26.0
  - psycopg2==2.9.11
  - PyJWT==2.12.1
  - sqlparse==0.5.5
  - tzdata==2025.3
  - whitenoise==6.12.0
- Actualización de docker-compose.yml y agregado de contenedor postgres
- Merge branch develop into main #1