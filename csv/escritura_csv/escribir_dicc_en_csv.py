import csv
# --------------------------------------------------------------
def csv_escritor(csv_out, csv_in):
    with open(csv_out, 'w', encoding='utf-8', newline='') as manejador:
        escritor = csv.DictWriter(manejador, fieldnames=csv_cabeceras(csv_in))
        escritor.writeheader()
        escritor.writerows(csv_datos(csv_in))
# --------------------------------------------------------------
def csv_cabeceras(csv_in):
    with open(csv_in, 'r') as manijero:
        return next(csv.reader(manijero))
# --------------------------------------------------------------
def csv_datos(csv_in):
        with open(csv_in, 'r') as manijero:
            return list(csv.DictReader(manijero))
# --------------------------------------------------------------

csv_entrada = 'titanic_corto.csv'
csv_salida = 'Nuevo_15.csv'

csv_escritor(csv_salida, csv_entrada)