import modulo

# Llama a la función ingresar_nombres_apellidos()
nombres, apellidos = modulo.ingresar_nombres_apellidos()
print("Nombres:", nombres)
print("Apellidos:", apellidos)

# Llama a la función pedir_tipo_seguro()
tipo_seguro = modulo.pedir_tipo_seguro()
print("Tipo de seguro:", tipo_seguro)

# Llama a la función es_mayor_edad()
es_mayor = modulo.es_mayor_edad()
if es_mayor:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
