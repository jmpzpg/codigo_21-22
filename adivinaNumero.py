from random import randrange
min = 10
max = 50
num_oculto = randrange(min,max) # dev num aleatorio entre min y max
num_introducido = 0

for contador in range(1,10,1):
    num_introducido = int(input(f'Di un número entre {min} y {max}: '))    # input dev una cadena y tenemos que convertirla a entero
    #print(num_introducido)

    if num_introducido == num_oculto:
        print(f'Acertaste, y el número de intentos fueron {contador}')
        break
    elif num_introducido < num_oculto and contador < 9:
        print('Es mayor. Sigue intentándolo')
    elif num_introducido > num_oculto and contador < 9:
        print('Es menor. Sigue intentándolo')

if num_introducido != num_oculto:
    print('Has perdido')
