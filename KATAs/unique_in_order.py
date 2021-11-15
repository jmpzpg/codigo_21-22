""" https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

Implement the function unique_in_order which takes as argument a sequence and 
returns a list of items without any elements with the same value next to each other and 
preserving the original order of elements.

    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1,2,2,3,3])       == [1,2,3]

"""


def unique_in_order(iterable: str):
    cadena_a_lista = list(iterable)
    lista_salida = []
    if cadena_a_lista != []:
        lista_salida.append(cadena_a_lista[0])
        for i in cadena_a_lista:
            if i != lista_salida[len(lista_salida)-1]:
                lista_salida.append(i)
    return lista_salida



#y = unique_in_order_total('AABBcddAB')
x = unique_in_order('AABBcddAB')
#print(y)
print(x)



#---------------------------------------------------------------------------



def unique_in_order_total(iterable: str):
    lista_salida = []
    cadena_a_lista = list(iterable)
    for i in cadena_a_lista:
        if i not in lista_salida:
            lista_salida.append(i)
    return lista_salida

def unique_in_order2(iterable: str):
    cadena_a_lista = list(iterable)
    lista_salida = []
    if cadena_a_lista != []:
        lista_salida.append(cadena_a_lista[0])
        for i in range(len(cadena_a_lista)):
            if i != 0:
                if cadena_a_lista[i] != lista_salida[len(lista_salida)-1]:
                    lista_salida.append(cadena_a_lista[i])
    return lista_salida


