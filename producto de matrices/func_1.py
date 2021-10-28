def func_dame_vector(col,H):
    matriz = H
    iteracion = len(matriz[0])
    v_aux = []
    for i in range(iteracion):
        v_aux.append(matriz[i][col])
    return(v_aux)

def func_multiplica_vectores(v1,v2):
    elem = 0
    for c in range(len(v1)):
        elem += v1[c] * v2[c]
    return(elem)

matriz_M = [[1,2],[3,4]]
matriz_H = [[4,3],[2,1]]
producto_MxH = []
for f in range(len(matriz_M[0])):
    fila_aux = []
    for i in range(len(matriz_H[0])):
        lista_aux = func_dame_vector(i,matriz_H)
        print(lista_aux)
        fila_de_M = matriz_M[f]
        print(fila_de_M)
        elem_matriz_prod = func_multiplica_vectores(fila_de_M,lista_aux)
        print(elem_matriz_prod)
        fila_aux.append(elem_matriz_prod)
        print(fila_aux)
    producto_MxH.append(fila_aux)

print(producto_MxH)