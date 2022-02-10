def capital_indexes(cad):
    salida = []
    for i in range(len(cad)):
        if cad[i] in ['A','B','C','D','E','F','G','H','I','J','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            salida.append(i)
    return salida
print(capital_indexes("HelLo"))