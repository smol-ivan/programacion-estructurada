"""def verificar_archivo(nombre_archivo):
    from os.path import isfile
    existe = False
    while not existe:
        if isfile(nombre_archivo):
            f = open(nombre_archivo, )
"""
def verificar_archivo(nombre_archivo):
    try:
        file = open(nombre_archivo, 'r')
        # Funciones para agregar producto o eliminar o eliminar
        # quiza sea bueno almacenar los datos del archvo en una variable, trabajarlos en otra funcion
        # para al final guardar todos los camios
        # del modulo para agregar o eliminar, guardar todos los cambios en una/s variables y sobreescribir
        file.close()
    except FileExistsError:
        print('El archivo no existe.')
        # funcion para crear un archivo si asi se necesita


#para las funciones que almacenan productos, tengo que tener otra funcion que tenga la plantilla para cada producto y en la funcion de agregar escoger que tipo de producto/plantilla escoger y despues preguntar con inputs por las caracteristicas de los productos, la funcion que pregunta por las caracteristicas puede recibir esas caracteristicas de la funcion que tiene la plantilla de los catalogos. en caso de no poder, que sea una funcion de inputs por catalogo

#Abrir el archivo leerlo, agregar/eliminar y luego cerrar
# o abrirlo, almacenar lo leido, cerrar el archivo, en otra funcion modificar lo del archivo, llamar a una funcion que sobreescriba los datos