def ingresar_nombres_apellidos():
    nombres = input("Ingrese sus nombres: ")
    apellidos = input("Ingrese sus apellidos: ")
    return nombres, apellidos

def pedir_tipo_seguro():
    tipo_seguro = input("Ingrese el tipo de seguro que tiene: ")
    return tipo_seguro

def es_mayor_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        return True
    else:
        return False
