# Prueba 2 - FileProcessor 

El objetivo del proyecto es analizar archivos en formatos comunes como CSV y DICOM, además de explorar el contenido de carpetas.

### 1. Instalar dependencias desde bash

cd P2_File_Processor
pip install -r requirements.txt


### 2. Ejecutar el proyecto

python3 test_processor.py


### 3. Probar cualquier archivo

Para probar cualquier archivo asegurate que este dentro de la carpeta selecionada como path
y luego en los parametros envia el nombre con formato del archivo especifico

#### Analizar un nuevo archivo CSV
processor.read_csv(filename="ejemplo.csv", summary=True)
#### Leer otro DICOM
processor.read_dicom(filename="ejemplo.dcm", extract_image=True)


### 4. Reportes
En la carpeta reports se guardan los reportes generados por la prueba


### 5. Registro de errores
Todos los errores se registran automáticamente en el archivo logs.txt.
Esto incluye:
* Archivos no encontrados
* Formatos no compatibles
* Problemas al leer datos
