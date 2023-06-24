"""
12. Reconocer los tipos de cada dato en la lista creadas y mostrarla en consola (type())
"""
lista = [4.44,5.44,6.44,7.44,False,8.44]

for i in range(0,len(lista)):
    dato = type(lista[i])
    print("El dato en la posicion {} es de tipo: {}".format(i,dato))