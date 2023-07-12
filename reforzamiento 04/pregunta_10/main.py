"""
PREGUNTA N°10
Crear una función donde se permitirá guardar el nombre, apellido y
edad de un usuario en un fichero (agenda.txt), cada usuario tiene que
estar guardado en una línea diferente y cada dato de una persona tiene
que estar separados por comas
"""
def funcion():
    nombre = str(input('Escriba su nombre: '))
    apellido = str(input('Escriba su apellido: '))
    edad = str(input('Escriba su edad: '))

    file = open("my_files/agenda.txt", "a+")
    file.write(nombre + ' ,'+apellido + ', '+edad+'\n')
    file = open("my_files/agenda.txt", "r")
    file.close()
    return 'Archivo guardado exitosamente!!!'

print(funcion())