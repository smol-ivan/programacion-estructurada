def agregar_producto(opcion):
    return print('Hola, aqui agregas un producto: ', opcion)

def mostrar_catalogo(opcion):
    return print('Hola, aqui muestras algun catalogo: ', opcion)

def buscar_catalogo(opcion):
    if opcion == 1:
        diccionario = 'Peliculas' # Llama a la funcion correspondiente por diccionario
    elif opcion == 2:
        diccionario = 'Series'
    else:
        diccionario = 'Todo'

catalogo = [
    {'Peliculas' : [
        {'Titulo': 'Nemo', 'Año' : 2003, 'Director' : 'Andrew Stanton'}, 
       {'Titulo': 'Buscando a Dory', 'Año' : 2016, 'Director' : 'Andrew Stanton'}]
       }]