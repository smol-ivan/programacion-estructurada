def options_selection(lista_opciones):
  option = False
  while not option:
      selection = input('Seleccione una opcion(num): ')
      if selection.isdigit() and int(selection) > 0 and int(selection) <= len(lista_opciones):
        option = True
      else: 
        print('Opcion invalida, intente de nuevo: ')
  return int(selection)

def options():
    lista = [{'menu principal': 
              {1: '~ Agregar un producto.', 
               2: '~ Buscar un producto.', 
               3: '~ Eliminar un producto.', 
               4: '~ Mostrar catálogo.', 
               5: '~ Cargar catálogo.', 
               6: '~ Guardar catálogo.', 
               7: '~ Salir.'}}, 
             {'menu agregar producto':
              {1: '~ Película', 
               2: '~ Serie', 
               3: '~ Documental', 
               4: '~ Evento deportivo en vivo',
               5: '~ Regresar'}}]
    return lista

def seleccionar_e_imprimir(list_num=0):
    selected_menu = options()[list_num]
    menu_title = list(selected_menu.keys())[0]
    menu_options = selected_menu[menu_title]
    
    print(f'~ {menu_title.capitalize()} ~')
    for key, value in menu_options.items():
        print(key, value)

def init():
   seleccionar_e_imprimir()  # Elige el número correspondiente al menú principal por defecto

init()
