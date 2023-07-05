"""
5. Obtén la cantidad total ítems que tienes en tu lista creada y mostrar el
resultado en consola. (Pista: len(lista))
"""

lista_01 = ["Economia", "Psicologia", "Administración Portuaria", "Tecnicas de Elocución y Redacción", "Contabilidad", "Administración financiera"]

lista_01.append("Tesis")
lista_01.append("Epistemologia")
lista_01.append("Herramientas informáticas")
lista_01.append("Investigación de mercados")

lista_01.remove("Tesis")
lista_01.remove("Epistemologia")

print("La cantidad de items es: {}".format(len(lista_01)))