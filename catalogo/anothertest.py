import manipulacion as use

def seleccion_opciones(opciones):
    option = False
    while not option:
        selection = input('Seleccione una opcion(num): ')
        if selection.isdigit() and int(selection) > 0 and int(selection) <= len(opciones):
            option = True
        else:
            print('Opcion invalida, intente de nuevo: ')
    return int(selection)

def imprimir_menu(menu):
    for key, value in menu.items():
        print(key, value)

def plantilla_menu(titulo, opciones=None):
    print(f'~{titulo}~')
    if opciones is not None:
        imprimir_menu(opciones)
    return

def opciones_menu(opcion):
    lista = [
        {1 : '~  Agregar un producto.', 
        2 : '~  Buscar un produto.', 
        3 : '~  Eliminar un producto.', 
        4 : '~  Mostrar catalogo.', 
        5 : '~  Cargar catalogo.', 
        6 : '~  Guardar catalogo.', 
        7 : '~  Salir.'}, 
        {1 : '~  Pelicula', 
        2 : '~  Serie', 
        3 : '~  Documental', 
        4 : '~  Evento deportivo en vivo',
        5 : '~  Regresar'}, 
        {1 : '~  Pelicula', 
        2 : '~  Serie', 
        3 : '~  Documental', 
        4 : '~  Evento deportivo en vivo',
        5 : '~  Todo',
        6 : '~  Regresar'}]
    return lista[opcion]

def principal():
    opciones = opciones_menu(0)
    plantilla_menu('Menu Principal', opciones)
    seleccion = seleccion_opciones(opciones)
    if seleccion == 1:
        agregar_producto()
    elif seleccion == 4:
        mostrar_catalogo()
    elif seleccion == 5:
        cargar_catalogo()

def agregar_producto():
    opciones = opciones_menu(1)
    plantilla_menu('Menu Agregar Producto', opciones)
    seleccion = seleccion_opciones(opciones)
    if seleccion != 5:
        use.agregar_producto(seleccion)
    else:
        principal()

def mostrar_catalogo():
    opciones = opciones_menu(2)
    plantilla_menu('Menu Mostrar Catálogo', opciones)
    seleccion = seleccion_opciones(opciones)
    if seleccion == 6:
        principal()

def cargar_catalogo():
    plantilla_menu('Agregar catalogo')
    print('Hola')
