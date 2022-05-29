import csv

from clase_crud_sqlite import Sqlite

bd = Sqlite('experimento_1.db')
#bd.crear_tabla('tabla_1','id integer primary key autoincrement,nombre text not null,edad int not null')
#print(bd.crear_tabla('tabla_2','id integer primary key autoincrement,ciudad text not null, pais text not null'))

# lista = [1,2,3,4,5]
# num = len(lista)
# val = 'VALUES(' + '?,'*(num-1) + '?)'


# lista = [1,2,3,4,5]
# b = tuple(lista)
# print(b)
# cad = 'VALUES('
# cad2 = cad + '?,'*3


with open('archivo.csv', 'r') as manejador:
    lectura = csv.reader(manejador)
    cabecera = next(lectura)
    fila1_datos = next(lectura)
    print(cabecera)
    print(fila1_datos)
    print(lectura)
    for elem in lectura:
        print(elem)

'''
with open('archivo.csv', 'r') as manejador:
    contenido = csv.reader(manejador)
    for elem in contenido:
        print(elem)


print(contenido)
'''