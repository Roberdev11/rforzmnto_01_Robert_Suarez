"""
PREGUNTA N°004
Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)
"""
string = "Hello Pythonista"
b=0
def division(a,b):
    try:
        result = a // b
        return ('El resultado de la division es: {}'.format(float(result)))
    except TypeError:
        return ('El dividendo no puede ser un texto')
    except ZeroDivisionError:
        return ('El divisor no puede ser cero')

print(division(string,b))