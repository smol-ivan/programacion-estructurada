#para las funciones que almacenan productos, tengo que tener otra funcion que tenga la plantilla para cada producto y en la funcion de agregar escoger que tipo de producto/plantilla escoger y despues preguntar con inputs por las caracteristicas de los productos, la funcion que pregunta por las caracteristicas puede recibir esas caracteristicas de la funcion que tiene la plantilla de los catalogos. en caso de no poder, que sea una funcion de inputs por catalogo

#Abrir el archivo leerlo, agregar/eliminar y luego cerrar
# o abrirlo, almacenar lo leido, cerrar el archivo, en otra funcion modificar lo del archivo, llamar a una funcion que sobreescriba los datos

def cargar_catalogo():
    while True:
        nombre_archivo = input('Ingrese el nombre del archivo a cargar: ')
        if nombre_archivo.strip() == '':
            print('El nombre del archivo no puede estar vacio. Intente de nuevo.')
            continue
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                catalogo = eval(contenido)
                return catalogo
        except FileNotFoundError:
            print(f"Archivo '{nombre_archivo}' no encontrado. Intente de nuevo.")

def guardar_catalogo(catalogo):
    from os.path import exists
    while True:
        nombre_archivo = input('Ingrese el nombre del archivo donde se guarde el catalogo: ')
        if nombre_archivo.strip() == '':
            print('El nombre del archivo no puede estar vacio. Intente de nuevo.')
            continue
        try:
            apertura = 'w' if exists(nombre_archivo) else 'x'
            with open(nombre_archivo, apertura) as archivo:
                archivo.write(repr(catalogo))
            return print(f'Catalogo guardado con exito en: "{nombre_archivo}"')
        except PermissionError:
            print(f"No tiene permisos para escribir en el archivo '{nombre_archivo}'. Intente de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el catálogo: {str(e)}")


dict = [
    {
        'Pelicula': [
            {'Titulo': 'Nemo', 'Año': 2003, 'Director': 'Andrew Stanton', 'Costo':{'Venta': '400', 'Renta': '200'}},
            {'Titulo': 'Buscando a Dory', 'Año': 2016, 'Director': 'Andrew Stanton', 'Costo':{'Venta': '400', 'Renta': '200'}}
        ]
    },
    {
        'Serie': [
            {'Titulo': 'Breaking Bad', 'Año': 2008, 'Creador': 'Vince Gilligan'},
            {'Titulo': 'Game of Thrones', 'Año': 2011, 'Creador': 'David Benioff, D. B. Weiss'}
        ]
    },
    {
        'Documental' : [
            {'Titulo': 'Hongos Fantasticos', 'Director/a': 'Paul Staments', 'Tema': 'Drogradiccion', 'Año': 2020, 'Costo':{'Venta': '400', 'Renta': '200'}}
        ]
    },
    {
        'Evento deportivo en vivo': [
            {'Titulo': 'UEFA Champions League', 'Deporte': 'Futbol', 'Fecha': '10/06/2023', 'Hora': '13:00', 'Lugar': 'Paris', 'Costo': {'Venta': '1000'}}
        ]
    }
]