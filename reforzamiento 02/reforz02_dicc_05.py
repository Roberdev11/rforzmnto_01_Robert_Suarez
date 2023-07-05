"""
5. Convertir tu diccionario a una lista y mostrar en consola
el tipo de datos final que tiene.
"""

diccionario = {"nombre" : "robert", "edad" : 23, "salario" : 5000}

transformacion = list(diccionario.items())

for i in range(0,len(transformacion)):
    valor = transformacion[i]
    print("La tupla N° {} es de tipo: {}".format(i,type(valor)))

