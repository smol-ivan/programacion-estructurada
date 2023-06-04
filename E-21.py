def recibir_datos_persona():
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    cumpleanos = input('Cumpleanos(DD-MM-AAA):')

    return nombre, apellido, cumpleanos

def recibir_datos_contacto():
    numero = input('Numero: ')
    email = input('Email: ')

    return numero, email

def crear_contacto(numero, email, persona):
    contacto = {'contacto': persona, 'Numero': numero, 'email': email}
    return contacto

def crear_persona(nombre, apellido, cumpleanos):
    persona = {'persona': {'nombre': nombre, 'apellido': apellido, 'cumpleanos': cumpleanos}}
    return persona

def directorio():
    directorio = []
    agregar = False
    while not agregar:
        respuesta = input('Desea agregar un nuevo contacto? (SI-NO):')
        if respuesta.lower() == 'si':
            agregar = True
            nombre, apellidos, numer