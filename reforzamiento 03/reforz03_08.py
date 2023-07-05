class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'dni': dni
        }
        self.contactos.append(contacto)
        print("Contacto agregado exitosamente.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No hay contactos en la agenda.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print(f"DNI: {contacto['dni']}")
                print("-------------------------")

    def buscar_contacto(self, dni):
        for contacto in self.contactos:
            if contacto['dni'] == dni:
                print("Contacto encontrado:")
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print(f"DNI: {contacto['dni']}")
                return

        print("No se encontró ningún contacto con el DNI proporcionado.")


# Ejemplo de uso
mi_agenda = Agenda()
mi_agenda.agregar_contacto("Juan Perez", "123456789", "juan@example.com", "12345678")
mi_agenda.agregar_contacto("María López", "987654321", "maria@example.com", "87654321")
mi_agenda.mostrar_contactos()
mi_agenda.buscar_contacto("12345678")

