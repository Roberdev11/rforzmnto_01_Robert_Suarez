"""
2. Convierte tu diccionario a una lista y mostrar el tipo de datos final
convertido en consola.
"""
diccionario = {"nombre" : "robert", "edad" : 23, "salario" : 5000}

transformacion = list(diccionario.items())

print(transformacion)
print(type(transformacion))