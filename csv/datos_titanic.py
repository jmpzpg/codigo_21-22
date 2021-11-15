import os
import csv
ruta = '/home/jmpp/codigo/codigo_21-22/csv/'

def leer_dict():
    csv_in = open(ruta + 'archivo.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict


muertos = 0
supervivientes = 0

datos = leer_dict()
for i in datos:
    dicc = {}
    dicc = i
    a = dicc.keys()
    if a['campo2'] == '1':
        supervivientes += 1
    else:
        muertos += 1

       


print('muertos = ' + str(muertos))
print('supervivientes = ' + str(supervivientes))