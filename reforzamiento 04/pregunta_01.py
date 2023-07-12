"""
PREGUNTA N°001
Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:

suma = 80 + “Hola Pythonista"
"""
valor_1 = 80
valor_2 = "Hola Pythonista"
def suma (x,y):
    try:
        return ('La suma de los valores es: {}'.format(x + y))
    except TypeError:
        return "Ingrese un valor numerico de la suma"

print(suma(valor_1,valor_2))