def insercion(lista, actual):
    lista_out = list(lista)
    for i in range(len(lista)):
        if lista_out[actual] < lista_out[i]:
            lista_out.insert(i, lista_out.pop(actual))
            if actual == len(lista_out)-1:
                break
    return lista_out


def ordena_lista(lista):
    salida = []
    for posicion in range(len(lista)-1):
        posicion += 1
        salida = insercion(lista, posicion)
    return salida


# ===================================
lista1 = [3,2,1]
lista_desordenada = [4,3,2,10,12,1,5,6] 
print(ordena_lista(lista1))
print(lista1)
print(ordena_lista(lista_desordenada))
