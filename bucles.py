for i in range(10) :
    print( f'Hola mundo {i}')

for i in range(5,10) :
    print( f'Hola mundo {i}')

for i in range(5,10,2) :
    print( f'Hola mundo {i}')

for i in range(1,100,2) : # solo los impares de 0 a 100
    print( f'Hola mundo {i}')

for i in range(100) :
    if i % 2 == 1 : # si i es impar
        print(i)
    

for i in range(100,0,-1) : # lo mismo pero desde 100 a cero
    if i % 2 == 1 : # si i es impar
        print(i)
