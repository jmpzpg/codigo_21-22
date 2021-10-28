producto_MxH = []
M = []
H = []
filas = 2
columnas = 2
total = filas * columnas

elementoM = 0
for i in range(filas):
    filaM = [] 
        
    for j in range(columnas):
        elementoM += 1
        filaM.append(elementoM)
    M.append(filaM)

elementoH = total
for i in range(filas):
    filaH = [] 
        
    for j in range(columnas):
        filaH.append(elementoH)
        elementoH -= 1
    H.append(filaH)

print('Matriz M:')
print(M)
print('Matriz H:')
print(H)

for i in range(filas):
    elem_matriz = 0
    fila_prod = []
    aux = M[i]
    for j in range(columnas):
        print('contadores i='+str(i)+' j='+str(j))
        a = aux[i][j]
        print('a: ' + str(a))
        b = H[j][i]
        print('b: ' + str(b))
        prod = a * b
        print('producto parcial: ' + str(prod))
        elem_matriz += prod
        print('elemento de la matriz: ' + str(elem_matriz))
    fila_prod.append(elem_matriz)
    for j in range(columnas):
        print('contadores i='+str(i)+' j='+str(j))
        a = aux[i][j]
        print('a: ' + str(a))
        b = H[j][i]
        print('b: ' + str(b))
        prod = a * b
        print('producto parcial: ' + str(prod))
        elem_matriz += prod
        print('elemento de la matriz: ' + str(elem_matriz))
    fila_prod.append(elem_matriz)
    print('fila resultado:')
    print(fila_prod)
    producto_MxH.append(fila_prod)

print('Matriz MxH:')
print(producto_MxH)




