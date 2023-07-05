"""
Crea una lista vacía (con 10 posiciones), pide sus valores y devuelve
la suma y la media de los números
"""
lista = []


for i in range(10):
    valor = float(input("Ingrese un número: "))
    lista.append(valor)

suma = sum(lista)
media = suma / len(lista)

print("La Suma es :", suma)
print("La Media es:", media)