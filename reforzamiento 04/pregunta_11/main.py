"""
PREGUNTA N°11
Crear una función que creará el archivo calificaciones.txt que contiene
las calificaciones de un curso.
Escribir un programa que contenga las siguientes funciones:
- Una función que guarde el nombre, 2 notas y el promedio (el
promedio lo calculará la función antes de escribirlo en el fichero)
- Y una función que leerá el fichero anterior y dirá si el alumno X,
aprobó o no, tener en cuenta que si tiene un promedio mayor a día
tendrá un mensaje de “Alumno X, aprobado” de lo contrario “Alumno
X, desaprobado”
"""

def guardar():
    nombre = str(input('Cual es el nombre del alumno?'))
    nota_1 = int(input('Cual es su nota 1?'))
    nota_2 = int(input('Cual es su nota 2?'))
    suma = (nota_1 + nota_2)
    promedio = suma // 2

    file = open("my_files/calificaciones.txt", "a+")
    file.write(nombre + ',' + str(nota_1) + ',' + str(nota_2) + ',' + str(promedio) + '\n')
    file.close()
    return 'Archivo guardado exitosamente!!!'

#print(guardar())

def verificar_aprobacion(nombre_alumno):
    # Modo (lectura)
    with open("my_files/calificaciones.txt", "r") as archivo:
        for linea in archivo:
            # Separa los campos por comas y extrae los valores
            campos = linea.strip().split(",")
            nombre = campos[0]
            promedio = int(campos[3])

            if nombre == nombre_alumno:
                if promedio > 10:
                    return f"Alumno {nombre}, aprobado"
                else:
                    return f"Alumno {nombre}, desaprobado"

    return "No se encontró el alumno especificado"

nombre_buscar = input("Ingrese el nombre del alumno a verificar: ")
resultado = verificar_aprobacion(nombre_buscar)
print(resultado)