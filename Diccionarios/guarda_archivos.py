from genericpath import isdir
import os
from config_rutas import RUTA_BASE, RUTA_CODIGO, MI_CARPETA

#nuevo_dir = os.chdir('/')

ruta_salida = RUTA_BASE + RUTA_CODIGO
if not os.path.exists(ruta_salida):
    os.makedirs(ruta_salida)
archivos = os.scandir(ruta_salida)
lista = []
for a in archivos:
    if a.is_file():
        if a.name.endswith('.py'):
            corte = a.name[:-3:]
            lista.append(corte)

manejador = open(ruta_salida + '/Mi_archivo.txt','w')

#manejador.write()

for i in range(0,len(lista),5):
    linea = ''
    for j in range(5):
        
        if lista[i]:
            linea += lista[i] + ', '
    #linea = lista[i] + ', ' + lista[i+1] + ', ' + lista[i+2] + ', ' + lista[i+3] + ', ' + lista[i+4]
    manejador.write(linea)
    pass

manejador.close()
#carpeta_trabajo = os.scandir(RUTA_BASE)