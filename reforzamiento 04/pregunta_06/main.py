"""
PREGUNTA N°006
 Creando un archivo principal donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones.
- La primera función cargará una un número entero que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo
"""

from operaciones import funcion1,suma
result_1 = funcion1()
result_2 = suma(result_1,45)

print('El resultado de la suma es: {}'.format(result_2))
