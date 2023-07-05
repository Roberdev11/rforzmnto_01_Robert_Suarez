"""
4. Elimina el key edad tipo de tu diccionario, incluyendo su valor.
del var[‘key’]
"""

diccionario = {"nombre" : "robert", "edad" : 23, "salario" : 5000}

#diccionario.pop("edad")
del diccionario["edad"]
print("Se elimino el key 'edad': {}".format(diccionario))