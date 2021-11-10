from genericpath import isdir
import os
import pprint
from config_rutas import RUTA_BASE, RUTA_CODIGO, MI_CARPETA


def clear():
    os.system('clear')


# Primero hay que abrir y leer del archivo de entrada una fila y la troceamos para tomar cada nombre de archivo
def func_leer_archivo(ruta, nom_archivo, modo_ap):
    lista_de_filas = []
    nuevo = open(ruta + nom_archivo, modo_ap)
    salida_lectura_archivo = nuevo.readlines()
    nuevo.close()
    return salida_lectura_archivo



clear()
x = func_leer_archivo(RUTA_BASE + RUTA_CODIGO, '/MiPrueba.txt', 'r')
#print(x)
clave = 0
dic_salida = {}
lista_general = []

for i in x:
    lista_de_fila = i[:-1:].split(',')
    for k in range(len(lista_de_fila)):
        dic_salida[clave] = lista_de_fila[k]
        clave += 1
        

pprint.pprint(dic_salida)