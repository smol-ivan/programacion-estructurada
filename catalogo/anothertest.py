
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

def menu_principal():
    opciones = opciones_menu(0)
    print('~Menu Principal~')
    imprimir_menu(opciones)
    seleccion = seleccion_opciones(opciones)
    if seleccion == 1:
        menu_agregar_producto()
    elif seleccion == 4:
        menu_mostrar_catalogo()     

def menu_agregar_producto():
    opciones = opciones_menu(1)
    print('~Menu Agregar Producto~')
    imprimir_menu(opciones)
    seleccion = seleccion_opciones(opciones)
    if seleccion == 5:
        menu_principal()

def menu_mostrar_catalogo():
    opciones = opciones_menu(2)
    print('~Menu Mostrar Catalogo~')
    imprimir_menu(opciones)
    seleccion = seleccion_opciones(opciones)
    if seleccion == 6:
        menu_principal()

def opciones_menu(opcion):
    lista = [{1 : '~  Agregar un producto.', 
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

menu_principal()