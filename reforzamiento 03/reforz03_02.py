class frase:
    def __init__(self):
        pass
    def revertir (self,texto):
        palabras = texto
        nuevo = list(palabras.split())
        revertido = list(reversed(nuevo))
        cadena = " ".join(revertido)
        return ('Cadena revertida: {}'.format(cadena))

frase_revertida = frase()
prueba1 = "Hola Pythonista, seguimos adelante"
print(frase_revertida.revertir(prueba1))
prueba2 = "Hola mundo 2023"
print(frase_revertida.revertir(prueba2))
