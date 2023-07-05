class persona:
    def __init__(self, nombre, edad, sueldo):
        self.nomb = nombre
        self.eda = edad
        self.remuneracion = sueldo
    def  mostrar_datos(self, pers_nombre, pers_edad, pers_remuneracion):
        self.nomb = str(pers_nombre)
        self.eda = int(pers_edad)
        self.remuneracion = float(pers_remuneracion)
        if self.eda >= 18:
            return 'El nombre de la persona es: {}, su edad es: {}, su remuneración es: {} y es mayor de edad'.format(self.nomb,self.eda,self.remuneracion)
        else:
            return 'El nombre de la persona es: {}, su edad es: {}, su remuneración es: {} y es menor de edad'.format(
                self.nomb, self.eda, self.remuneracion)
    def bonificacion(self):
        bonific = self.remuneracion * (20/100)
        return 'La bonificacion es: {}'.format(bonific)

individuo = persona('',0,0)

persona_nomb = "nicole"
persona_edad = 17
persona_remuneracion = 2000

print(individuo.mostrar_datos(persona_nomb, persona_edad, persona_remuneracion))
print(individuo.bonificacion())

persona_nomb = "juan"
persona_edad = 25
persona_remuneracion = 1000

print(individuo.mostrar_datos(persona_nomb, persona_edad, persona_remuneracion))
print(individuo.bonificacion())

