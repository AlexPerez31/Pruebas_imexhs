# Prueba 4 - Angular App

Aplicación desarrollada en Angular 19 para calcular el área de una mancha en una imagen binaria (Investigue y es un metodo similar al de Monte Carlo)

### 1. Requisitos y entorno
Este proyecto fue desarrollado en Angular 19. Es necesario tener instalado,
primero ingresa a la raiz del proyecto (comandos desde bash):

cd image-area-app

Node.js 18+
Angular CLI

Para usar el proyecto:

1. Clona o descarga el repositorio.
2. Instala las dependencias

npm install

3. Ejecuta el proyecto:

ng serve

Una vez en funcionamiento, puedes acceder a la aplicación en:

http://localhost:4200/


### 2. Uso de la aplicación

Para utilizar correctamente la aplicación, sigue estos pasos:

1. Carga una imagen binaria desde tu equipo (en blanco y negro).
2. Ajusta el número de puntos aleatorios con el slider (mínimo: 1000, máximo: 200000).
    Se recomienda usar imágenes de aproximadamente 500x500px para mejores resultados.
3. Haz clic en "Calcular" y automáticamente se estimará el área usando el método de Monte Carlo.
No podrás continuar al siguiente paso si no cargas una imagen.


### 3. Imágenes de prueba

En la carpeta /images (fuera del proyecto), se encuentran algunas imágenes de ejemplo listas para probar el sistem


### 4. Funcionalidades extra agregadas

Además del cálculo básico del área, se añadieron varias mejoras al proyecto:

* Historial persistente usando localStorage, para conservar resultados entre recargas.

* Tabla de resultados con: 
    Paginación
    Miniatura de la imagen cargada
    Fecha y hora en que se realizó el cálculo

* Botón para limpiar historial, en caso de que el usuario quiera reiniciar todo


### 5. Pruebas unitarias

Se incluyen pruebas automáticas usando el sistema de Angular:

1. Cada componente y el servicio principal (StainService) cuentan con su archivo de pruebas.
2. Se realizaron pruebas adicionales más allá de las generadas automáticamente.

Para ejecutarlas:

ng test


### 6. Documentación
Se generó documentación completa del proyecto con Compodoc.

Para visualizarla:

npm run docs

Luego accede en el navegador a:

http://127.0.0.1:8080