def buscar_categoria(categoria, catalogo):
    for i in catalogo:
        if categoria in i:
            return i[categoria]
    return None

def agregar_producto(catalogo, opcion):
    return print('Hola, aqui agregas un producto: ', opcion)

def mostrar_catalogo(catalogo, opcion):
    return print('Hola, aqui muestras algun catalogo: ', opcion)

def eliminar_producto():
    

def buscar_catalogo(catalogo, opcion):
    if opcion == 1:
        diccionario = 'Peliculas' # Llama a la funcion correspondiente por diccionario
    elif opcion == 2:
        diccionario = 'Series'
    else:
        diccionario = 'Todo'

