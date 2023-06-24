"""
7. Crear un diccionario con 6 departamentos en el país.
- Borrar cualquier departamento (uno) usando la palabra reservada del.
- Comprobar que no existe este departamento borrado dentro del diccionario.

"""

peru = {"departamentos":["Lima", "Cusco", "Puno", "Arequipa", "Loreto", "Cajamarca"]}


del peru["departamentos"][0]
print("Se elimino el departamento de 'Lima': {}".format(peru))