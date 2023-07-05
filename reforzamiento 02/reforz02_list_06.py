"""
6. Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista)
dentro de la lista.
"""
lista_01 = ["Economia", "Psicologia", "Administración Portuaria", "Tecnicas de Elocución y Redacción", "Contabilidad", "Administración financiera"]

lista_01.append("Tesis")
lista_01.append("Epistemologia")
lista_01.append("Herramientas informáticas")
lista_01.append("Investigación de mercados")

lista_01.remove("Tesis")
lista_01.remove("Epistemologia")

#Se agrega 'Economia' nuevamente
lista_01.append("Economia")
lista_01.append("Economia")

print("El curso de 'Economia' se repite {} veces".format(lista_01.count('Economia')))
