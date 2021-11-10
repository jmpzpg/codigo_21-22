from genericpath import isdir
import os
from config_rutas import RUTA_BASE, RUTA_CODIGO, MI_CARPETA

#nuevo_dir = os.chdir('/')



def clear():
    os.system('clear')




""" busca en la carpeta de la ruta todos los archivos .py y los dev en una lista sin el .py """
def func_busca_archivos(ruta, extension='.py'):  
    long_extension = len(extension)
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    archivos = os.scandir(ruta)
    lista = []
    for a in archivos:
        if a.is_file():
            if a.name.endswith(extension):
                corte = a.name[:-long_extension :]
                lista.append(corte)
    return lista

def func_agrupar_archivos(listado, numero):
    fila = ''
    for i in range(0,len(listado),numero):
        temp = listado[i:i+numero]
        fila += ','.join(temp) + '\n'
    return fila

def func_escribe_archivo(ruta, nom_archivo, modo_ap, fila):
    nuevo = open(ruta + nom_archivo, modo_ap)
    nuevo.write(fila)
    nuevo.close()
    





clear()
ruta_salida = RUTA_BASE + RUTA_CODIGO
x = func_busca_archivos(ruta_salida,'.py')
print(x)
f = func_agrupar_archivos(x,5)
print(f)
func_escribe_archivo(ruta_salida,'/MiPrueba.txt','w',f)



""" manejador = open(ruta_salida + '/Mi_archivo.txt','w')

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
 """