def func_dame_fila_prod_matrices(lista,matriz):
    elem_matriz = 0
    fila_prod = []
    aux = lista
    columnas = len(lista)
    for i in range(columnas):
        for j in range(columnas):
            print('contadores i='+str(i)+' j='+str(j))
            a = aux[j]
            print('a: ' + str(a))
            b = H[j][i]
            print('b: ' + str(b))
            prod = a * b
            print('producto parcial: ' + str(prod))
            elem_matriz += prod
            print('elemento de la matriz: ' + str(elem_matriz))
        fila_prod.append(elem_matriz)
        elem_matriz = 0
        for j in range(1,columnas):
            print('contadores i='+str(i)+' j='+str(j))
            a = aux[i]
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


lista = [1,2]
H = [[4,3],[2,1]]
fila_producto = func_dame_fila_prod_matrices(lista,H)