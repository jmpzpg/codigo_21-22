lista1 = [1,2,3]
lista2 = [1,2,3]
son_iguales = True
x = len(lista1)
y = len(lista2)

if x == y:                          # si las longitudes de ambas listas son iguales
    for i in range(x):
        if lista1[i] != lista2[i]:  # en cuanto encontramos un elemento de ambas que no sea igual
            son_iguales = False
            break
else:
    son_iguales = False

if son_iguales:
    print("las dos listas son iguales")
else:
    print("las dos listas son distintas")



