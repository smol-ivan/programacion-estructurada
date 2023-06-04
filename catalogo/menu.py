def menu():
    

  """
  def opciones_menu(num = 0):
      lista = [{'menu principal': 
                {1 : '~  Agregar un producto.', 
                2 : '~  Buscar un produto.', 
                3 : '~  Eliminar un producto.', 
                4 : '~  Mostrar catalogo.', 
                5 : '~  Cargar catalogo.', 
                6 : '~  Guardar catalogo.', 
                7 : '~  Salir.'}}, 
              {'menu agregar producto' :
                {1 : '~  Pelicula', 
                2 : '~  Serie', 
                3 : '~  Documental', 
                4 : '~  Evento deportivo en vivo',
                5 : '~  Regresar'}}]
      return lista[num]

  def imprimir_menu(lista):
      menu_seleccionado = opciones_menu()
      menu_titulo = list(menu_seleccionado.keys())[0]
      menu_opciones = menu_seleccionado[menu_titulo]

      print(f'~ {menu_titulo.capitalize()} ~')
      for key, value in menu_opciones.items():
        print(key, value)
  """

def seleccion_opciones(opciones):
    option = False
    while not option:
        selection = input('Seleccione una opcion(num): ')
        if selection.isdigit() and int(selection) > 0 and int(selection) <= len(opciones):
            option = True
        else:
            print('Opcion invalida, intente de nuevo: ')
    return int(selection)