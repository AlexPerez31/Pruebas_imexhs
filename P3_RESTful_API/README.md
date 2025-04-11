# Prueba 3 - RESTful API con Django

API RESTful para procesar resultados de imágenes médicas. 
El sistema permite almacenar datos procesados, normalizarlos, calcular promedios, consultar entradas por filtros y realizar operaciones CRUD completas, todas con logs y documentadas.


### 1. Requisitos y entorno

Este proyecto fue desarrollado en **Django 4.2.20** con **PostgreSQL** como base de datos. Es necesario tener Python 3.9+ instalado.

1. Clona o descarga el proyecto.
2. Crea y activa un entorno virtual:

python -m venv env
env\Scripts\activate  # En Windows

3. Instala todas las dependencias con:

pip install -r requirements.txt


### 2. Base de datos de ejemplo

En la carpeta utils, encontrarás un archivo de respaldo llamado:

medical_api_db

Puedes usarlo como base para restaurar en tu instancia de PostgreSQL.


### 3. Ejecutar el servidor

python manage.py runserver

Una vez en funcionamiento, puedes acceder a los endpoints a través de:

http://localhost:8000/api/


### 4. Pruebas con Postman

Dentro de la carpeta utils también se encuentra una colección Postman con pruebas listas para usar.

Solo importa la colección en Postman y ejecuta las solicitudes.


### 5. Carpeta de logs

Todos los eventos importantes (POST, errores, validaciones) se registran automáticamente en:

/logs/api.log

Ahí se guarda el historial de cada petición procesada por la API.


### 6. Tests unitarios y automatizados

/tests/

Donde hay pruebas unitarias básicas. Para ejecutarlas:

pytest


### 7. Documentación

Se generaron dos documentaciones interactivas usando Swagger y Redoc:

* Swagger UI:
http://localhost:8000/swagger/

* Redoc:
http://localhost:8000/redoc/