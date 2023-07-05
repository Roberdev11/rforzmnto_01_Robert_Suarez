def rango(a,b):
    rango_cuadrados = [n ** 2 for n in range(a+1,b)]
    return rango_cuadrados
print('Los numero comprendidos entre 10 y 15 al cuadrado son: {}'.format(rango(10,15)))