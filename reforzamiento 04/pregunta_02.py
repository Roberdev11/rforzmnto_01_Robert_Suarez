"""
PREGUNTA N°002
Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]
"""

valor_lista = 10
def buscar_lista(x):
    try:
        lista = [2, 6, 10, 4, 5, 23, 1]
        return ('El valor segun la lista es: {}'.format(lista[x]))
    except IndexError:
        return ('El indice registrado está fuera del rango válido')


print(buscar_lista(valor_lista))