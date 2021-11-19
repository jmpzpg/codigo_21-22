import csv

# csv header
cabeceras = ['nombre', 'area', 'codigo_pais2', 'country_code3']

# csv data
rows = [
    {'nombre': 'Albania',
    'area': 28748,
    'codigo_pais2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]

with open('uevo_3.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=cabeceras)
    writer.writeheader()
    writer.writerows(rows)
