"""
PREGUNTA N°15
Queremos consumir un JSON que se encuentra alojado en la nube el cual
nos traerá los datos de una persona como la edad, nombre, email, dirección
o nombre de la compañía en donde trabaja.
La url a consumir usando Python es la siguiente:
https://jsonplaceholder.typicode.com/users
Obtener respectivamente los valores necesarios para formar la siguiente
oración:

Bienvenido “nombre” “apellido”, usted tiene “edad” años. El correo que
nos proporcionó es “correo” y la compañía actual donde trabaja se llama
“nombreCompañía”. Dentro de sus datos también encontramos una website
que es: “nombreWeb”
Finalmente agregar un usuario al json obtenido pero sólo con los datos de
nombre, apellido, edad y compañía donde trabaja y finalmente mostrarlo en
consola (sólo ese usuario nuevo)

"""

import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
data = response.json()

nombre = data[9]['name'].split()[0]  # Obtener el primer nombre
apellido = data[9]['name'].split()[1]  # Obtener el apellido
correo = data[9]['email']
nombreCompañia = data[9]['company']['name']
nombreWeb = data[9]['website']

oracion = f"Bienvenido {nombre} {apellido}. El correo que nos proporcionó es {correo} y " \
          f"la compañía actual donde trabaja se llama {nombreCompañia}. " \
          f"Dentro de sus datos también encontramos una website que es: {nombreWeb}"

print(oracion)

# Nuevo usuario
nuevo_usuario = {
    "name": "Robert Suarez",
    "company": {
        "name": "Indecopi"
    }
}

data.append(nuevo_usuario)

print(data)

