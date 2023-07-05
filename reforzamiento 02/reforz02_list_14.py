"""
14. Elimina un elemento por dos índices existentes y ya no por el valor.
"""

lista = [4.44,5.44,6.44,7.44,False,8.44]

del lista[-1]
print("Se elimina el ultimo elemento utilizando el indice [-1]: {}".format(lista))

del lista[0]
print("Se elimina el primer elemento utilizando el indice [0]: {}".format(lista))
