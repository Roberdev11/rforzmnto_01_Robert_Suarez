"""
PREGUNTA N°12
 Crear una función decoradora que dará los buenos días antes de
ejecutar una función a ser decorada y luego de ser ejecutada lanzará
un mensaje diciendo “Hasta luego”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje “Soy ‘nombre’”
"""

def decorador_saludo(funcion):
    def wrapper():
        print("Buenos días")
        funcion()
        print("Hasta luego")
    return wrapper

@decorador_saludo
def saludar():
    nombre = input("Ingrese su nombre: ")
    print(f"Soy '{nombre}'")

saludar()


