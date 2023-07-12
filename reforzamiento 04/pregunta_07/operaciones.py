import random
def funcion_generar():
   lista = []
   for i in range(100):
      lista.append(random.randrange(1, 100))
   return (lista)

def ordenar_numbers(nueva_lista):
   list_orden = list(nueva_lista)
   list_orden.sort()
   return (list_orden)

