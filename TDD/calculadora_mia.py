def sumar(cadena):
    lista = cadena.split(',')

    for i in lista:
        if not  i.isdigit():
            return 'Error: caracter no numerico'

    if len(lista) > 2:
        return "Error: Demasiados numeros"

    elif len(lista) == 2:
        return True


def mas_de_dos_numeros_da_error():
    return sumar('1,2,3')

def dos_numeros_devuelve_true():
    return sumar('1,2')

def caracter_no_numerico_da_error():
    return sumar('1,a')


print(mas_de_dos_numeros_da_error())
print(dos_numeros_devuelve_true())
print(caracter_no_numerico_da_error())