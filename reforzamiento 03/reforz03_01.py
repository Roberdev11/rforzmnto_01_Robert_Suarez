class pregunta1:
    def __init__(self):
        self.resultado = 0

    def ingresardato(self):
        valor = int(input('Ingrese un valor numérico: '))
        self.resultado = valor

    def cubo (self):
        cubo = self.resultado ** 3
        return cubo
    def cuadrado(self):
        cubo = self.cubo()
        cuadrado = cubo ** 2
        return cuadrado

operacion_basica = pregunta1()

operacion_basica.ingresardato()

print('El numero ingresado al cubo es: {}'.format(operacion_basica.cubo()))
print('El numero ingresado al cuadrado es: {}'.format(operacion_basica.cuadrado()))