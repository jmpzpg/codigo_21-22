import random

def func_genera_equipos_v02(alumnos, miembros):
    random.shuffle(alumnos)
    equipos = []

    for i in range(0,len(alumnos),miembros):
        equipos.append(alumnos[i:i+miembros])

    return equipos


gente = [1,2,3,4,5,6,7,8,9]
for x in range(5):
    x = func_genera_equipos_v02(gente,3)
    print(x)