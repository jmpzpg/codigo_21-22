def double_letters(cad):
    salida = False
    for i in range(len(cad)-1):
        if cad[i] == cad[i+1]:
            salida = True
    return salida

print(double_letters('hello'))
print(double_letters('mono'))
