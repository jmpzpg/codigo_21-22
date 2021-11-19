import csv
ruta = '/home/jmpp/codigo/codigo_21-22/csv/'

def csv_write():
    cabeceras = ['simb', 'car']
    with open('nuevo_1.csv', 'w', newline='') as csv_write:
        #escritor = csv.writer(csv_write)
        escritorDic = csv.DictWriter(csv_write, fieldnames=cabeceras) 
        #escritor.writerow(['Lo mejor de ambos mundos'])
        a = ['Lo peor de ambos mundos']
        lista_dicc = [{'simb':'letra a', 'car': 'letra b'},{'simb':'letra x', 'car':'letra y'}]
        #escritor.writerow(a)
        #escritor.writerow(['jueves'] + ['viernes'])
        #escritor.writerows([a])
        escritorDic.writeheader()
        escritorDic.writerows(lista_dicc)

csv_write()