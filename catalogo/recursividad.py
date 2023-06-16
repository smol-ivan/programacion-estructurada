def imprimir_producto(producto):
    for key, value in producto.items():
        print(f'{key}: {value}')

def buscar_series(lista, palabras_clave):
    coincidencias = []
    for serie in lista:
        for palabra_clave in palabras_clave:
            if palabra_clave.lower() in serie['Titulo'].lower() or \
               str(palabra_clave) == str(serie['Año']) or \
               palabra_clave.lower() in serie['Creador'].lower():
                coincidencias.append(serie)
                break
    return coincidencias

def buscar_documentales(lista, palabras_clave):
    coincidencias = []
    for documental in lista:
        for palabra_clave in palabras_clave:
            if palabra_clave.lower() in documental['Titulo'].lower() or \
               str(palabra_clave) == str(documental['Director/a']) or \
               palabra_clave.lower() in documental['Tema'].lower() or \
               palabra_clave.lower() in documental['Año'].lower():
                coincidencias.append(documental)
                break
    return coincidencias

def buscar_serie_recursivo(lista, palabras_clave):
    series_encontradas = buscar_series(lista, palabras_clave)
    if len(series_encontradas) == 1:
        return series_encontradas[0]
    elif len(series_encontradas) > 1:
        print("Series encontradas:")
        for serie in series_encontradas:
            print(imprimir_producto(serie))

        nuevas_palabras_clave = input("Ingrese otra palabra clave: ").split()

        return buscar_serie_recursivo(series_encontradas, nuevas_palabras_clave)
    else:
        return None

# Ejemplo de uso
series = [
    {'Titulo': 'Breaking Bad', 'Año': 2008, 'Creador': 'Vince Gilligan'},
    {'Titulo': 'Game of Thrones', 'Año': 2011, 'Creador': 'David Benioff, D. B. Weiss'},
    {'Titulo': 'Breaking Dawn', 'Año': 2008, 'Creador': 'Stephanie Meyer'}
]

palabras_clave = input("Ingrese una palabra clave: ").split()

serie_encontrada = buscar_serie_recursivo(series, palabras_clave)

if serie_encontrada:
    print("Serie encontrada:")
    print(serie_encontrada)
else:
    print("No se encontró ninguna serie.")

