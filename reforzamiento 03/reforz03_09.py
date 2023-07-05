class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.__sueldo = int(sueldo)  # encapsulamiento

    def calcular_impuestos(self):
        if self.__sueldo > 4000:
            return 'Debe pagar impuestos: {}'.format(self.__sueldo * 0.10)
        else:
            return 'No debe pagar impuestos'

nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
sueldo = float(input("Ingrese el sueldo del empleado: "))

empleado = Empleado(nombre, edad, sueldo)
print(empleado.calcular_impuestos())
