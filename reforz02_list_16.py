"""
16. Mostrar sólo los datos comprendidos entre la posición 10 y 35
"""
lista = []
for i in range(1,101):
    lista.append(i)

del lista[10:36]


print(lista)