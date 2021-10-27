import pprint
cols = 10
filas = 10
matriz = []

""" for i in range(filas):
    fila = []
    for j in range(cols):
        #fila.append(f'{i}-{j}')
        fila.append(str(i)+'-'+str(j))
    matriz.append(fila)
matriz[5][5] = 'agua'
pprint.pprint(matriz)

print(matriz[5][6])
 """

for i in range(filas):
    fila = []
    for j in range(cols):
        fila.append('X')
        #fila.append(str(i)+'-'+str(j))
    matriz.append(fila)

for i in range(filas):
    linea = ''
    for j in range(cols):
        linea += matriz[i][j]
    print(linea)