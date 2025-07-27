# #Proyecto Django: Mi Blog

Este proyecto es una aplicación web desarrollada con Django 5.2.4 y Python 3.13 que permite crear y administrar un blog simple. Incluye funcionalidades para gestionar Autores, Categorías y Posts, con búsqueda de publicaciones y un panel administrativo mediante Django Admin.

# # Descripción

La aplicación cuenta con las siguientes características:

- Modelos para Autor, Categoría y Post con sus respectivos campos.
- Formularios para crear y validar nuevos autores, categorías y posts.
- Búsqueda de posts por título en la página principal.
- Plantillas HTML organizadas con herencia para facilitar el mantenimiento.
- Administración completa mediante el panel de Django Admin.
- Uso de base de datos SQLite por defecto para facilitar el desarrollo.

# # Estructura del Proyecto

- `manage.py`: Script para administrar el proyecto.
- Carpeta `mi_proyecto`: Configuración global de Django (settings, urls, wsgi).
- Carpeta `accounts`: Aplicación que contiene modelos, vistas, formularios, URLs y plantillas específicas.
- Carpeta `templates`: Plantillas HTML organizadas por aplicación (`accounts`).
- Base de datos SQLite (`db.sqlite3`) en la raíz del proyecto.

## Requisitos

- Python 3.13 o superior
- Django 5.2.4

## Instalación y Ejecución

* Clonar el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DE_LA_CARPETA>

* Crear y activar un entorno virtual (opcional pero recomendado):

En Windows:

python -m venv env
.\env\Scripts\activate

En macOS/Linux:

python3 -m venv env
source env/bin/activate



* Instalar las dependencias:

pip install django==5.2.4


* Ejecutar las migraciones para crear las tablas en la base de datos:

python manage.py migrate


* Crear un superusuario para acceder al panel de administración:

python manage.py createsuperuser

Sigue las instrucciones para establecer usuario y contraseña.


* Iniciar el servidor de desarrollo:

python manage.py runserver


* Abrir el navegador y acceder a:

Página principal: http://127.0.0.1:8000/

Panel admin: http://127.0.0.1:8000/admin/




* * Uso 

Desde la página principal puedes buscar posts por título y navegar las publicaciones.

Crear nuevos autores, categorías y posts a través de formularios accesibles en las URLs:

/autor/nuevo/

/categoria/nueva/

/post/nuevo/


Gestionar todos los modelos desde el panel administrativo.


* * Notas

Este proyecto está pensado para entornos de desarrollo. Para producción, se recomienda configurar servidores WSGI/ASGI adecuados y bases de datos robustas.

Las configuraciones relevantes están en mi_proyecto/settings.py, donde se define el uso de templates, rutas estáticas y base de datos.



---

AUTOR:  Claudio Gonzalez 
FECHA:  Julio 2025