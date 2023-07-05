"""
3. Agrega un nuevo key llamado “dni” con su respectivo valor
y luego mostrar el valor de salario en consola.
var[‘key’] = tuValor
"""
diccionario = {"nombre" : "robert", "edad" : 23, "salario" : 5000}

diccionario["DNI"]="73824416"


print("El valor del sueldo es: {}".format(diccionario.get("salario")))

