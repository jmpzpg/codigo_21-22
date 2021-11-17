import os
import csv
ruta = '/home/jmpp/codigo/codigo_21-22/csv/'

def leer_dict():
    csv_in = open(ruta + 'titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict


""" muertos = 0
supervivientes = 0
hombres_v = 0
mujeres_v = 0
hombres_m = 0
mujeres_m = 0 """
tercera_clase = 3
segunda_clase = 2
primera_clase = 1
""" tercera_clase_v = 0
tercera_clase_m = 0
segunda_clase_v = 0
segunda_clase_m = 0
primera_clase_v = 0
primera_clase_m = 0 """

dicc_salida = {'supervivientes': 0, 'h_v': 0, 'm_v': 0, 'clase1_h_v': 0, 'clase1_m_v': 0,
    'clase2_h_v': 0, 'clase2_m_v': 0, 'clase3_h_v': 0, 'clase3_m_v': 0,
    'muertos': 0, 'h_m': 0, 'm_m': 0, 'clase1_h_m': 0, 'clase1_m_m': 0,
    'clase2_h_m': 0, 'clase2_m_m': 0, 'clase3_h_m': 0, 'clase3_m_m': 0 }

lista_diccionarios = leer_dict()

for diccionario in lista_diccionarios:
    if diccionario['Survived'] == '1':
        if diccionario['Sex'] == 'male':
            if diccionario['Pclass'] == tercera_clase:
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