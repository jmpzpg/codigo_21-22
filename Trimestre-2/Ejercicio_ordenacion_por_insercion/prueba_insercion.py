def insercion():
    lista_desordenada = [5,2,3]
    actual = 1
    for i in range(len(lista_desordenada)):
        if lista_desordenada[actual] < lista_desordenada[i]:
            lista_desordenada.insert(i, lista_desordenada.pop(actual))
    return lista_desordenada      

# ============================

print(insercion())
