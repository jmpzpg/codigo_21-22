import csv
ruta = '/home/jmpp/codigo/codigo_21-22/csv/'

def csv_write():
    with open(ruta + 'nevo_1.csv', 'a') as csv_write:
        escritor = csv.writer(csv_write)
        escritor.writerow(['jueves'] * 10 + ['viernes'])
        escritor.writerow(['Lo mejor de ambos mundos'] * 3)

csv_write()