"""
Borra el primer ítem de la lista usando debidamente su índice
"""

lista_01 = ["Economia", "Psicologia", "Administración Portuaria", "Tecnicas de Elocución y Redacción", "Contabilidad", "Administración financiera"]

lista_01.append("Tesis")
lista_01.append("Epistemologia")
lista_01.append("Herramientas informáticas")
lista_01.append("Investigación de mercados")

lista_01.remove("Tesis")
lista_01.remove("Epistemologia")

#Se elimina la lista por indice
del lista_01[0]

print("Se elimino el primer curso 'Economia' de la siguiente lista: {}".format(lista_01))