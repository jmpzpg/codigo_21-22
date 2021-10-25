from random import randrange, gauss

alumnos = ['Alan','Alejandro','Antonio','Fernando','Jose','Juan','Rafa','Raul']
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
 
print(equipos)
