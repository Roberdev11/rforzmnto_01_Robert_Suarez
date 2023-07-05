"""
1. El valor de ‘¡HI TuNombre!’ imprimirlo por pantalla, el texto debe ser un string y
deberás guardarlo en una variable llamada mi_saludo.
Tu nombre debe estar en otra variable.
"""
TuNombre = "Robert"
mi_saludo = "¡HI {}!".format(TuNombre)
print(mi_saludo)

"""
2. Crea una variable tipo int. Luego, multiplica por 10 y restarle 10. 
Debes hacer todo estoo en dos pasos. Finalmente mostrar el resultado por pantalla.
"""
number = 50
result = (number*10)-10
print(result)

"""
3. Crear una variable tipo string y poder luego sumarla con otra variable 
tipo int, para esto convertir una de las variables. Mostrar la suma en pantalla.
"""

var_1="80"
var_2 = 90

convertir = int(var_1)

suma = convertir +var_2
print(suma)

"""
4. Hallar el volumen de una esfera, cada dato requerido para hallar 
el volumen debe estar en una variable. Mostrar el volumen por pantalla.
"""
constante = 4/3
pi = 3.1416
radio = 2
radio_cubo = pow(radio,3)
volumen = float(constante*pi*radio_cubo)

print(volumen)

"""
5. Crear un programa que partiendo de un sueldo en una variable, 
sepamos si es par o impar. Utilizar módulo y condicional.

"""

sueldo = input("Escriba su sueldo: ")
digito = sueldo[-1]
cadena_par = ["0","2","4","6","8"]

if digito in cadena_par:
    print("Su sueldo es PAR")
else:
    print("Su sueldo es IMPAR")

"""
6. Calcular la media de 5 datos (floats), cada dato debe estar en una variable y 
la media también. Mostrar el resultado en pantalla.
"""
dato1 = 23.30
dato2 = 24.40
dato3 = 25.50
dato4 = 26.60
dato5 = 27.70

suma = (dato1,dato2,dato3,dato4,dato5)

media = sum(suma)/5

print("La media de los datos es:", media)

"""
7. De 3 números asignados (tú los propones) a 3 variables, se pide hallar la 
suma de los valores de los módulos con 3, 5, y 7 respectivamente, mostrar en 
pantalla el valor de la suma.
"""
numero_1 = int(input("Primer numero es:"))
numero_2 = int(input("Segundo numero es:"))
numero_3 = int(input("Tercer numero es:"))

modulo1 = numero_1 + 3
modulo2 = numero_2 + 5
modulo3 = numero_3 + 7

print("La primera suma es: {}, La segunda suma es: {}, La tercera suma es: {}".format(modulo1,modulo2,modulo3))
"""
8. Usando la condicional if imprimir por pantalla si una lista está vacía o no, 
probar con una lista vacía y otra con una lista vacía.
"""
list_vacia = []
list_completa = [1,2,3]

if len(list_vacia) == 0:
    print("La lista esta vacia")
else:
    print("La lista no esta vacia")

if len(list_completa) == 0:
    print("La lista esta vacia")
else:
    print("La lista es completa")

"""
9. Elevar al exponente de 4 un número que su valor estará asignado a una variable y 
luego restar este mismo valor multiplicado por dos (usar pow). 
Mostrar el resultado en pantalla.
"""
valor = input("Escribe un numero: ")
numero = int(valor)
resultado = (pow(numero,4) - numero) * 2
print(resultado)

"""
10. Crear un diccionario con los siguientes key: nombre, carrera, edad y año de nacimiento, 
mostrar en pantalla el valor de este diccionario.
"""
diccionario = {"nombre": "Robert", "carrera": "Administración","edad": 27, "año_nacimiento": 1995}

print(diccionario)

"""
11. Identificar que tipo de dato se obtiene al elevar un número a la exponente de 5 y luego 
dividirlo por 10. Mostrar el resultado en pantalla.
"""

valor_register = input("Digite un numero: ")
valor_number = int(valor_register)
result_final = pow(valor_number,5)/10

print(type(result_final))