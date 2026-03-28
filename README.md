# Sistema de Chatbots y Dashboard de gestión

## Descripción

**Sistema de Chatbots que incluye:**
- Chatbot de atención al cliente (**Instagram**).
- Chatbot terapéutico con IA (**WhatsApp**).
- **Dashboard web** para la gestión de sesiones psicológicas. 

> Utiliza **n8n** para la automatización de flujos de conversación y **Django** como backend y panel de administración.

---

## Diagrama de Flujo de la Aplicación

> [Diagrama de flujo](https://excalidraw.com/#json=QO_P94ZifjeQv-pqLbBe1,7PE0po91e8gi6y1Jhg5TPg)

>[!TIP] 
>Se recomienda abrir el diagrama en una nueva pestaña para una mejor visualización.

---

## Tecnologías
- **Django(Python)**: Framework web para el backend y panel de administración.
- **n8n**: Plataforma de automatización para gestionar los flujos de conversación.
- **PostgreSQL**: Base de datos relacional para almacenar datos de usuarios y sesiones.
- **Docker**: Contenerización de la aplicación para facilitar su despliegue y desarrollo
- **Docker Compose**: Orquestación de los servicios de la aplicación.
- **HTML/CSS/JavaScript**: Para el desarrollo del frontend del dashboard.
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
├── n8n/
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Notas

- Los flujos de n8n se almacenan en el volumen `n8n_data`.
>[!NOTE] 
>Se puede usar un archivo `docker-compose.override.yml` para configurar un volumen externo para persistir los datos de n8n en caso de necesitarlo.

