# Prueba 1 - Torre de Hanói con Restricción de Colores

Este script resuelve una variante del clásico problema de la Torre de Hanói, donde además de la restricción de tamaño, **no se permite colocar discos del mismo color uno encima del otro**.

---

## Cómo probar nuevos casos

Para realizar pruebas personalizadas, simplemente reemplaza la variable `disks` dentro del archivo `main.py` por cualquier lista de tuplas con el siguiente formato:

```python
disks = [(tamaño, "color")]

Ejemplo:
disks = [(4, "rojo"), (3, "azul"), (2, "verde"), (1, "rojo")]

Para ejecutarlo ingresa a la carpeta desde bash

cd P1_Recursion_and_Colors

Y ejecuta

python3 main.py