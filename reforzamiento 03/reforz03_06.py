
class Alumno:
    def nombre_alumno(self, valor_nombre):
        nombre = str(valor_nombre)
        return 'El nombre del alumno es: {}'.format(nombre)

    def edad_alumno(self, valor_edad):
        edad = int(valor_edad)
        return 'La edad del alumno es: {}'.format(edad)

    def nota_alumno(self, valor_nota):
        nota = float(valor_nota)
        return 'La nota del alumno es: {}'.format(nota)

    def estado_alumno(self,estado):
        if estado >= 11:
            return 'El alumno esta aprobado'
        else:
            return 'El alumno esta desaprobado'


estudiante = Alumno()
estudiante_nombre = "Ronald"
estudiante_edad = 23
estudiante_nota = 10

print(estudiante.nombre_alumno(estudiante_nombre))
print(estudiante.edad_alumno(estudiante_edad))
print(estudiante.nota_alumno(estudiante_nota))
print(estudiante.estado_alumno(estudiante_nota))

estudiante_nombre = "Juan"
estudiante_edad = 27
estudiante_nota = 13
print(estudiante.nombre_alumno(estudiante_nombre))
print(estudiante.edad_alumno(estudiante_edad))
print(estudiante.nota_alumno(estudiante_nota))
print(estudiante.estado_alumno(estudiante_nota))

estudiante_nombre = "Luisa"
estudiante_edad = 21
estudiante_nota = 19
print(estudiante.nombre_alumno(estudiante_nombre))
print(estudiante.edad_alumno(estudiante_edad))
print(estudiante.nota_alumno(estudiante_nota))
print(estudiante.estado_alumno(estudiante_nota))
