
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


""" fila = [('x'*20)]

for i in range(20):
    x = fila
    print(x) """


""" fila = []
columna = []

for i in range(20):
    for j in range(20):
        fila[i] = columna.append('x')

pprint.pprint(fila) """