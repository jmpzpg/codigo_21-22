'''     Jose Manuel Perez Puig
Versión deprisa y corriendo para que funcionara. La versión 2 está mucho más optimizada
'''
def insercion(lista, actual):
    for i in range(len(lista)):
        if lista[actual] < lista[i]:
            lista.insert(i, lista.pop(actual))
            if actual == len(lista)-1:
                break
    return lista

def ordena_lista(lista_in):
    lista = list(lista_in)
    for posicion in range(len(lista)-1):
        posicion += 1
        lista = insercion(lista, posicion)
    return lista

# ===================================
lista1 = [3,2,1]
lista2 = [4,3,2,10,12,1,5,6] 
print(f'lista1 ordenada: {ordena_lista(lista1)} y Lista2 ordenada: {ordena_lista(lista2)}')
print(f'Lista1 original: {lista1} y Lista2 original: {lista2}')
