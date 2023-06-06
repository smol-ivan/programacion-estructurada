def verificar_archivo(nombre_archivo):
    from os.path import isfile
    existe = False
    while not existe:
        if isfile(nombre_archivo):
            f = open(nombre_archivo, )