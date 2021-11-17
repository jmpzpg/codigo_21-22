import os
import csv
ruta = '/home/jmpp/codigo/codigo_21-22/csv/'

def leer_dict():
    csv_in = open(ruta + 'titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict


muertos = 0
supervivientes = 0
hombres_v = 0
mujeres_v = 0
hombres_m = 0
mujeres_m = 0

lista_diccionarios = leer_dict()

for diccionario in lista_diccionarios:
    if diccionario['Survived'] == '1':
        if diccionario['Sex'] == 'male':
            supervivientes += 1
            hombres_v += 1
        else:
            supervivientes += 1
            mujeres_v += 1
    else:
        if diccionario['Sex'] == 'female':
            muertos += 1
            mujeres_m +=1
        else:
            muertos += 1
            hombres_m += 1
 
print('Numero de muertos = ' + str(muertos))
print(f'Mujeres muertas = {mujeres_m}')
print(f'Hombres muertos = {hombres_m}')

print('Numero de supervivientes = ' + str(supervivientes))
print(f'Mujeres vivas = {mujeres_v}')
print(f'Hombres vivos = {hombres_v}')
