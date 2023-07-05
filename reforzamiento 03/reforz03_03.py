class Persona:
    def __init__(self):
        self.datos = {}

    def ingresar_nombre_apellido(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        self.datos['nombre'] = nombre
        self.datos['apellido'] = apellido

    def ingresar_edad(self):
        edad = input("Ingrese su edad: ")
        self.datos['edad'] = edad

    def imprimir_resultados(self):
        print('Los nombres y apellidos son: {} {} y la edad es: {}'.format(self.datos['nombre'],self.datos['apellido'],self.datos['edad']))

# Instanciar clase
persona = Persona()
persona.ingresar_nombre_apellido()
persona.ingresar_edad()
persona.imprimir_resultados()
