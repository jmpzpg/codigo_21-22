producto_MxH = []
M = []
H = []
filas = columnas = 3
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

print(M)
print(H)

for i in range(filas):
    elem_matriz = 0
    fila_prod = []
    for j in range(columnas):
        #print(M[i])
        a = M[i][j]
        b = H[i][j]
        prod = a * b
        elem_matriz += prod
        fila_prod.append(elem_matriz)
    producto_MxH.append(fila_prod)

print(producto_MxH)




