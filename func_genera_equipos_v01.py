import random as rd 

def func_genera_equipos(alumnos):
    personas = alumnos.copy()           # ahora trabajamos con una copia y no modificaremos la lista original
    rd.shuffle(personas)
    equipos = []
    num_equipos = len(personas) // 2

    for i in  range(num_equipos):
        eq = []
        eq.append(personas.pop())
        eq.append(personas.pop())
        equipos.append(eq)

    if len(personas) > 0:
        equipos[num_equipos - 1].append(personas.pop())

    return equipos


alumnos = [1,2,3,4,5,6,7,8,9]
for x in range(5):
    x = func_genera_equipos(alumnos)
    print(x)


    """ alumnos = ['Alan','Alejandro','Antonio','Fernando','Jose','Juan','Rafa','Raul']
    rango = len(alumnos)
    equipos = []
    emparejamiento_de_2 = ' con '
    emparejamiento_de_3 = ' y '

    for i in range(rango//2):
    
        for j in range(2):
            ind_aleatorio = randrange(rango)
            if j == 0:
                pareja1 = alumnos.pop(ind_aleatorio)
            else:
                pareja2 = alumnos.pop(ind_aleatorio)
            rango -= 1
        
        if rango == 1:
            equipos.append(pareja1 + emparejamiento_de_2 + pareja2 + emparejamiento_de_3 + alumnos.pop(0))
        else:
            equipos.append(pareja1 + emparejamiento_de_2 + pareja2)
 
    return(equipos)
 """