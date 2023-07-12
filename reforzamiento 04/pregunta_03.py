"""
PREGUNTA N°003
Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:

persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']

"""
valor_persona = 'profesion'
def buscar_diccionario(valor):
    try:
        persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
        return ('El valor de la clave {} del diccionario es: {}'.format(valor,persona[valor]))
    except KeyError:
        return ('El valor de la clave no existe')

print(buscar_diccionario(valor_persona))