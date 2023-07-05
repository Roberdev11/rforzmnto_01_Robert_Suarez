"""
8. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario.
- Mostrar en consola los valores de su variable final (ya sea diccionario o lista).
"""

diccionario = {"nombre" : "robert", "edad" : 23, "salario" : 5000}

diccionario["carrera"] = "administracion"

print("El valor de la variable carrera es: {}".format(diccionario.get("carrera")))