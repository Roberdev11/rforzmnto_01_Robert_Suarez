import math
class circulo:
    def __init__(self,radio):
        self.rad = radio

    def ingrese_radio(self):
        try:
            self.rad = float(input('Escriba el radio del circulo: '))
        except ValueError:
            raise ValueError("El radio debe ser un valor numérico.")

    def area(self):
        area_circulo = math.pi * pow(self.rad,2)
        return area_circulo

    def perimetro(self):
        perimetro_circulo = 2 * math.pi * self.rad
        return perimetro_circulo

result = circulo(0)
result.ingrese_radio()
print('El valor del area 1 es: {}'.format(result.area()))
print('El valor del perimetro 1 es: {}'.format(result.perimetro()))
result.ingrese_radio()
print('El valor del area 2 es: {}'.format(result.area()))
print('El valor del perimetro 2 es: {}'.format(result.perimetro()))