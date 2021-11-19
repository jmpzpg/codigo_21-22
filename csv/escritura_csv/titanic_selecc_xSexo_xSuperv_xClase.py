import csv
ruta = '/home/jmpp/codigo/codigo_21-22/csv/'
# --------------------------------------------------------------
def csv_escritor(csv_out, csv_in):
    with open(csv_out, 'w', encoding='utf-8', newline='') as manejador:
        escritor = csv.DictWriter(manejador, fieldnames = csv_cabeceras(csv_in))
        escritor.writeheader()
        escritor.writerows(csv_seleccionar_datos(csv_in))
# --------------------------------------------------------------
def csv_cabeceras(csv_in):
    with open(csv_in, 'r') as manijero:
        return next(csv.reader(manijero))
# --------------------------------------------------------------
def csv_datos(csv_in):
        with open(csv_in, 'r') as manijero:
            return list(csv.DictReader(manijero))
# --------------------------------------------------------------
def csv_seleccionar_datos(csv_in):
    lista_dicc_salida = []
    for diccionario in csv_datos(csv_in):
       
        if diccionario['Sex'] == sexo and diccionario['Survived'] == supervivencia and diccionario['Pclass'] == clase:
            lista_dicc_salida.append(diccionario)

    return lista_dicc_salida


csv_entrada = ruta + 'titanic.csv'
csv_salida = 'Nuevo_20.csv'
parametros_seleccion = {}
gen = input('Introduce el género a buscar. "m" para hombres y "f" para mujeres: ')
if gen == 'f':
    sexo = 'female'
elif gen == 'm':
    sexo = 'male'
else:
    print('Por favor, introduce un carácter válido')

sup = input('Introduce si sobrevivió "1" o falleció "0": ')
if sup == '1' or sup == '0':
    supervivencia = sup
else:
    print('Por favor, introduce un carácter válido. "0" o "1"')

cla = input('Introduce la clase a buscar. "1" para la Primera, "2" la Segunda y "3" la Tercera: ')
if cla == '1' or cla == '2' or cla == '3':
    clase = cla
else:
    print('Por favor, introduce un carácter válido. "1" o "2" o "3"')


#sexo = 'female'       # 'male' o 'female'
#superviviente = '0' # '1' o '0', para superviviente y fallecido respectivamente
#clase = '2'         # '1' o '2' o '3', para las clases de pasajeros

csv_escritor(csv_salida, csv_entrada)