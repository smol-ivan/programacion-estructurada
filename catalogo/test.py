def menu_principal():
    opciones = {1 : 'Agregar un producto.', 
                    2 : 'Buscar un produto.', 
                    3 : 'Eliminar un producto.', 
                    4 : 'Mostrar catalogo.', 
                    5 : 'Cargar catalogo.', 
                    6 : 'Guardar catalogo.', 
                    7 : 'Salir.'}
    imprimir_menu(opciones)
    opcion = opcion_menu(len(opciones))
    if opcion == 1:
        menu_agregar_producto()
    elif opcion == 4:
        menu_mostrar_catalogo()

def menu_agregar_producto():
    opciones = {1 : 'Pelicula', 
                    2 : 'Serie', 
                    3 : 'Documental', 
                    4 : 'Evento deportivo en vivo',
                    5 : 'Regresar'}
    imprimir_menu(opciones)
    opcion = opcion_menu(len(opciones))
    if opcion == 5:
        menu_principal()

def menu_mostrar_catalogo():
    opciones = {1 : 'Pelicula', 
                    2 : 'Serie', 
                    3 : 'Documental', 
                    4 : 'Evento deportivo en vivo',
                    5 : 'Todo',
                    6 : 'Regresar'}
    imprimir_menu(opciones)
    opcion = opcion_menu((len(opciones)))
    if opcion == 6:
        menu_principal()

def opcion_menu(options):
    option = False
    while not option:
        selection = input('Ingrese la operacion a realizar(num): ')
        if selection.isdigit() and int(selection) > 0 and int(selection) <= options:
            option = True
        else:
            print('Opcion invalida, intente de nuevo: ')
    return int(selection)

def imprimir_menu(menu):
    for key, value in menu.items():
        print(key, value)

menu_principal()