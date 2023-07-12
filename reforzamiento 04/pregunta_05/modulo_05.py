def validar_nombre(usuario):
    texto = usuario
    if len(texto) <= 6:
        return "El nombre de usuario debe contener al menos 7 caracteres"
    elif len(texto) >= 13:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    elif not texto.isalnum():
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return True