"""
PREGUNTA N°009
Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido.
"""

def funcion():
    numero = int(input('Escriba un numero entero entre 1 y 20: '))
    if 1 <= numero <= 20:
        file = open("my_files/tabla.txt", "w")
        for i in range(1, numero + 1):
            valor = i * numero
            file.write(str(i)+str("x")+str(numero)+str("= ")+str(valor)+'\n')
        file = open("my_files/tabla.txt", "r")
        file.close()
        return 'Archivo guardado existosamente!!!'
    else:
        print('Error: Escriba un numero entero entre 1 y 20')
        return funcion()

print(funcion())
