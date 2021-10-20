cadena = "uno, dos, tres, cuatro, cinco"
resultado_esperado = []
fin = len(cadena)
inicio_trozo = 0
for i in range(fin):
    if cadena[i] == ',':
        a = cadena[inicio_trozo:i]
        resultado_esperado.append(a)
        inicio_trozo = i + 2

resultado_esperado.append(cadena[inicio_trozo:fin])    
print(resultado_esperado)