# API RESTful de Temperaturas (Weather API)

API desarrollada con **Django REST Framework (DRF)** para gestionar registros de temperatura de diferentes ciudades. Implementa un sistema CRUD completo con autenticación por tokens y permisos granulares.

##  Características

* **CRUD Completo:** Crear, Leer, Actualizar y Eliminar registros de temperatura.
* **Autenticación por Token:** Seguridad integrada para operaciones de escritura.
* **Permisos Personalizados:**
    * **Público:** Cualquiera puede ver (GET) las temperaturas.
    * **Privado:** Solo usuarios autenticados pueden crear, editar o borrar (POST, PUT, DELETE).
* **Validaciones:** Control de unicidad por ciudad y tipos de datos.
* **Unit Testing:** Cobertura de pruebas automatizadas.

## Tecnologías

* Python 3.x
* Django 5.x
* Django REST Framework
* SQLite (Base de datos)

##  Instalación y Configuración

Sigue estos pasos para levantar el proyecto en local:

### 1. Clonar el repositorio

git clone [https://github.com/Alenpiera/weather_api.git](https://github.com/Alenpiera/weather_api.git)

cd weather_api

### 2. Crear entorno virtual

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Instalar dependencias

pip install -r requirements.txt

### 4. Migraciones y Superusuario

python manage.py migrate
python manage.py createsuperuser
# Sigue las instrucciones para crear tu usuario admin

### 5. Ejecutar servidor

python manage.py runserver


### Documentación de EndpointsLa API responde en http://127.0.0.1:8000/api/

Método  Endpoint            Descripción                     Requiere Auth
GET     /temperatures/      Listar todas las ciudades       ❌ No
POST    /temperatures/      Registrar nueva ciudad          ✅ Sí
GET     /temperatures/      {id}/Ver detalle de una ciudad  ❌ No
PUT     /temperatures/      {id}/Actualizar registro        ✅ Sí
DELETE  /temperatures/      {id}/Eliminar registro          ✅ Sí
POST    /api-token-auth/    Obtener Token de Acceso         ❌ No

### Cómo autenticarse (Ejemplo)

Envía un POST a /api-token-auth/ con tu username y password.

Copia el token que recibes.

En tus peticiones protegidas (POST/PUT/DELETE), añade el Header:

Key: Authorization

Value: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

### Ejecutar Pruebas (Testing)

El proyecto incluye pruebas unitarias para validar la seguridad y los endpoints.

python manage.py test

 Autor
Enrique Piedrahita 
