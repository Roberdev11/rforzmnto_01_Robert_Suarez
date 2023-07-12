"""
PREGUNTA N°14
Crear un decorador donde imprimirá la cantidad de argumentos que
tiene la función a decorar usando *args y **kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es”
mensaje post “La función decoradora terminó de ejecutarse
correctamente”
"""

def contador_argumentos(func):
    def wrapper(*args, **kwargs):
        print("La cantidad de argumentos que tiene la función es:", len(args) + len(kwargs))
        result = func(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return result
    return wrapper

@contador_argumentos
def suma(*args, **kwargs):
    total = sum(args)
    for value in kwargs.values():
        total += value
    return total

resultado = suma(4, 1, 10, 2, 50, 64,20)


