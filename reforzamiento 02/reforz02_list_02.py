"""
2. Agregar 4 Objetos nuevos a tu lista (append).
"""

lista_01 = ["Economia", "Psicologia", "Administración Portuaria", "Tecnicas de Elocución y Redacción", "Contabilidad", "Administración financiera"]
#lista_02 = ["Tesis", "Epistemologia", "Herramientas informáticas", "Investigación de mercados"]

#lista_01.extend(lista_02)

lista_01.append("Tesis")
lista_01.append("Epistemologia")
lista_01.append("Herramientas informáticas")
lista_01.append("Investigación de mercados")

print("Se agrego a la lista los cursos 'Tesis', 'Epistemologia', 'Herramientas informaticas', 'Investigación de mercados': {}".format(lista_01))
print("Numero de objetos en la lista: {}".format(len(lista_01)))
