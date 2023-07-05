"""
3. Quita 2 elementos de tu nueva lista ítems por valor, no por índice.
"""

lista_01 = ["Economia", "Psicologia", "Administración Portuaria", "Tecnicas de Elocución y Redacción", "Contabilidad", "Administración financiera"]

lista_01.append("Tesis")
lista_01.append("Epistemologia")
lista_01.append("Herramientas informáticas")
lista_01.append("Investigación de mercados")

lista_01.remove("Tesis")
lista_01.remove("Epistemologia")

#del lista_01[6:8]


print("Se quitaron 'Tesis' y 'Epistemologia' de la lista: {}".format(lista_01))