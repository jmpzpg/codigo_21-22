def add_dots(cad):
    lista = list(cad)
    return '.'.join(lista)

def remove_dots(cad):
    return cad.replace('.', '')

print(remove_dots(add_dots('test')))
