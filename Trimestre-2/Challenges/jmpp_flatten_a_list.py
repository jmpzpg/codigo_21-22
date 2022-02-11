def flatten(lista):
    salida = []
    for elem in lista:
        for e in elem:
            salida.append(e)
    return salida


print(flatten([[1,2], [3,4]]))