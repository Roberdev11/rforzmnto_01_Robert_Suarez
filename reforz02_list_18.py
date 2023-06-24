"""
18. Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes repetidos
 (los cuales son impares dentro del rango indicado y que no sea el último impar).
- Empezando desde 1 y no 0.
- Agregar un cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del.
"""

numeros = [(n*2)+1 for n in range(0, 15)]
numeros.append(9.5)
numeros.append(9.5)
numeros.append(9.5)
numeros.sort()
numeros.insert(3,"cadena")
print(numeros)
del numeros[3]
print(numeros)
