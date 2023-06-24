"""
4. Invierte y muestra en consola tu lista de cursos.
"""

lista_01 = ["Economia", "Psicologia", "Administración Portuaria", "Tecnicas de Elocución y Redacción", "Contabilidad", "Administración financiera"]

lista_01.append("Tesis")
lista_01.append("Epistemologia")
lista_01.append("Herramientas informáticas")
lista_01.append("Investigación de mercados")

lista_01.remove("Tesis")
lista_01.remove("Epistemologia")

lista_01.reverse()
print("Lista invertida: {}".format(lista_01))