def buscar_catalogo(categoria, catalogo):
    for i in catalogo:
        if categoria in i:
            return i[categoria]
    return None

