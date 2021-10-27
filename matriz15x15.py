import pprint
cols = 15
filas = 15
matriz = []

for i in range(filas):
    fila = []
    for j in range(cols):
        fila.append('X')
    matriz.append(fila)
pprint.pprint(matriz)