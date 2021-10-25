from ast import Num


def dame_el_doble(x):
    if type(x) in [int,float,complex]:
        return x*2
    else:
        return None

#num = int(input("dame un numero para doblarlo: "))
num = 1.7
print('el doble de ' + str(num) + ' es: ' + str(dame_el_doble(num)))