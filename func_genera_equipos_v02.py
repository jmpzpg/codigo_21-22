import random

def func_genera_equipos_v02(alumnos, miembros):
    random.shuffle(alumnos)
    equipos = []
    num_equipos = len(alumnos) // 2
    pos_final_parejas = 0

    for i in range(0,len(alumnos),miembros):
        equipos.append(alumnos[i:i+miembros])

    

    if ( len(alumnos) % miembros != 0 ):
        equipos[num_equipos - 1].append(alumnos[len(alumnos)-1:])  # linea inacabada

    return equipos

gente = [1,2,3,4,5,6,7,8,9]
for x in range(5):
    x = func_genera_equipos_v02(gente,4)
    print(x)