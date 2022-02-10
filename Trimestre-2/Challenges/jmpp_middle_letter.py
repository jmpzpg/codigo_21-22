def mid(cad):
    salida = ''
    resto = len(cad) % 2
    final = len(cad)
    if resto == 1:
        c = final // 2
        salida = cad[c]    

    return salida


print(mid('abcde'))
