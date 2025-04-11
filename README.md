Realice todas las cuatro pruebas establecidas tratando de documentar todo lo más posible cada uno de los archivos y funciones, para de esta forma lograr un código más familiar, fácil de revisar y que demuestre mis habilidades y metodologías al momento de desarrollar.

**Cada carpeta tiene su propio archivo README donde se especifica como ejecutar y probar todos los proyectos, además de que agregue explicaciones extra de funcionalidades y la arquitectura usada**

## Prueba 1 y 2:
Para estas pruebas tarte de que el output fuera lo más similar posible a los ejemplos datos en el documento pdf.


## Prueba 3:
Esta prueba la realicé usando Django y además de cumplir con todos los requisitos necesario también quise agregar algunas funcionalidades extra que serían un plus en el proyecto y mejorarían la escalabilidad como demostración de mis habilidades en arquitectura de desarrollo y escalabilidad de proyectos a largo plazo:

* Documentación de API: Integré documentación interactiva con Swagger y ReDoc, accesible desde el navegador. Esto permite explorar todos los endpoints disponibles y probarlos desde la misma interfaz.
* Logs personalizados: Configuré un sistema de logging que registra cada acción relevante en un archivo logs/api.log, incluyendo errores, entradas exitosas y advertencias por datos inválidos.
* Tests unitarios con Pytest: Como valor agregado, implementé pruebas básicas con pytest para asegurar que el comportamiento de la API se mantenga estable al recibir distintos tipos de datos.
* Colección Postman: Incluí una colección de Postman para facilitar las pruebas de todos los endpoints sin necesidad de escribir manualmente cada solicitud.
* Copia de la base de datos: También agregué un backup de la base de datos en la carpeta utils/medicalbd para poder importar los datos fácilmente si se desea replicar el entorno.


## Prueba 4:
Para esta prueba además de cumplir con todas las funcionalidades descritas, quise agregar algunos extras:

* Debido a que todo funcionara en una sola pagina entonces no agregue el archivo routes o share que en este caso en innecesario
* También separé toda la lógica de negocio con la interfaz de usuario, para eso lo dividí en las carpetas /features/ y /pages/
* Como la prueba es solo de frontend y no hay backend o persistencia de datos quise agregar una funcionalidad con el LocalStorage para asi persistir los datos momentáneamente
* Agregue documentación dinámica a través de un enlace generado
* Agregue el punto opcional de realizar algunas pruebas unitarias# Pruebas_imexhs
