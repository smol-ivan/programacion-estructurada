"""catalogo = [
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

def buscar_categoria(categoria, catalogo):
    for item in catalogo:
        if categoria in item:
            return item[categoria]
        
productos = buscar_categoria('Peliculas', catalogo)

for i in productos:
    """

def imprimir_series(diccionario):
    if 'Serie' in diccionario:
        series = diccionario['Serie']
        print("Series:")
        for serie in series:
            print("- Titulo:", serie['Titulo'])
            print("  Año:", serie['Año'])
            print("  Creador:", serie['Creador'])
    else:
        print("No se encontraron series en el diccionario.")

# Ejemplo de uso con tu diccionario
diccionario = {
    'Serie': [
        {'Titulo': 'Breaking Bad', 'Año': 2008, 'Creador': 'Vince Gilligan'},
        {'Titulo': 'Game of Thrones', 'Año': 2011, 'Creador': 'David Benioff, D. B. Weiss'}
    ]
}

imprimir_series(diccionario)