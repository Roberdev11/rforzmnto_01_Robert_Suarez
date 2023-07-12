"""
PREGUNTA N°008:
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a
mostrarla.
"""
from operaciones import cargar_valor, raiz_cuadrada, cuadrado, cubo

resultado = cargar_valor()
raiz = raiz_cuadrada(resultado)
numero_cuadrado = cuadrado(resultado)
numero_cubo = cubo(resultado)

print("La raiz cuadrada del numero ingresado es: {}".format(raiz))
print("El cuadrado del numero ingresado es: {}".format(numero_cuadrado))
print("El cubo del numero ingresado es: {}".format(numero_cubo))