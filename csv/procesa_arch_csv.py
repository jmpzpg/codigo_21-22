import os
import csv

print(os.getcwd())
ruta = '/home/jmpp/codigo/codigo_21-22/csv/'
def leer_csv_normal():
    with open(ruta + 'archivo.csv') as csv_in:
        filas = csv_in.readlines()
        for f in filas:
            print(f)
            #print(f.split())


leer_csv_normal()

def leer_dict():
    csv_in = open(ruta + 'archivo.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict

# salida = leer_dict()
# print(salida)