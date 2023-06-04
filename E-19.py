def length_password():
    auth = False
    while not auth:
        length = input('Elija el largo de la contraseña: ')
        if length.isnumeric() and int(length) >= 8:
          auth = True
    return length

def uppercase_letter():
    auth = False
    while not auth:
        seleccion = input('Quisiera incluir Mayusculas? (SI/NO): ')
        if seleccion.isalpha():
            if seleccion.lower() == 'si':
                letter = True
                auth = True
            elif seleccion.lower() == 'no':
                letter = False
                auth = True
    return letter 

def lowercase_letter():
    auth = False
    while not auth:
        seleccion = input('Quisiera incluir Minusculas? (SI/NO): ')
        if seleccion.isalpha():
            if seleccion.lower() == 'si':
                letter = True
                auth = True
            elif seleccion.lower() == 'no':
                letter = False
                auth = True
    return letter 

def numbers():
    auth = False
    while not auth:
        seleccion = input('Quisiera incluir numeros? (SI/NO): ')
        if seleccion.isalpha():
            if seleccion.lower() == 'si':
                letter = True
                auth = True
            elif seleccion.lower() == 'no':
                letter = False
                auth = True
    return letter 

def special_characters():
    auth = False
    while not auth:
        seleccion = input('Quisiera incluir caracteres especiales? (SI/NO): ')
        if seleccion.isnumeric():
            if seleccion.lower() == 'si':
                letter = True
                auth = True
            elif seleccion.lower() == 'no':
                letter = False
                auth = True
    return letter

"""def password_generator():
    return """

