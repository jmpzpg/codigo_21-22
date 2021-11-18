import os
import csv
import pprint
ruta = '/home/jmpp/codigo/codigo_21-22/csv/'

def leer_dict():
    csv_in = open(ruta + 'titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict

tercera_clase = '3'
segunda_clase = '2'
primera_clase = '1'
muertos = supervivientes = 0
hombres_v = mujeres_v = hombres_m = mujeres_m = 0
tercera_clase_v = tercera_clase_m = segunda_clase_v = segunda_clase_m = primera_clase_v = primera_clase_m = 0
superv_h_c1 = superv_h_c2 = superv_h_c3 = 0
superv_m_c1 = superv_m_c2 = superv_m_c3 = 0
muerto_h_c1 = muerto_h_c2 = muerto_h_c3 = 0
muerto_m_c1 = muerto_m_c2 = muerto_m_c3 = 0

dicc_salida = {'supervivientes': 0, 'h_v': 0, 'm_v': 0, 'clase1_h_v': 0, 'clase1_m_v': 0,
    'clase2_h_v': 0, 'clase2_m_v': 0, 'clase3_h_v': 0, 'clase3_m_v': 0,
    'muertos': 0, 'h_m': 0, 'm_m': 0, 'clase1_h_m': 0, 'clase1_m_m': 0,
    'clase2_h_m': 0, 'clase2_m_m': 0, 'clase3_h_m': 0, 'clase3_m_m': 0 }

lista_diccionarios = leer_dict()

for diccionario in lista_diccionarios:
    superv = diccionario['Survived']
    sexo = diccionario['Sex']
    clase = diccionario['Pclass']
    if superv == '1':                           # si es superviviente
        supervivientes += 1
        dicc_salida['supervivientes'] += 1
        if sexo == 'male':                      # si es superviviente y hombre
            hombres_v += 1
            dicc_salida['h_v'] += 1

            if clase == primera_clase:          # si es superviviente, hombre y de primera clase
                primera_clase_v += 1
                superv_h_c1 += 1
                dicc_salida['clase1_h_v'] += 1
            elif clase == segunda_clase:        # si es superviviente, hombre y de segunda clase
                segunda_clase_v += 1
                superv_h_c2 += 1
                dicc_salida['clase2_h_v'] += 1
            else:                               # si es superviviente, hombre y de tercera clase
                tercera_clase_v += 1
                superv_h_c3 += 1
                dicc_salida['clase3_h_v'] += 1        
        else:                                   # si es superviviente y mujer
            mujeres_v += 1
            dicc_salida['m_v'] += 1

            if clase == primera_clase:          # si es superviviente, mujer y de primera clase
                primera_clase_v += 1
                superv_m_c1 += 1
                dicc_salida['clase1_m_v'] += 1
            elif clase == segunda_clase:        # si es superviviente, mujer y de segunda clase
                segunda_clase_v += 1
                superv_m_c2 += 1
                dicc_salida['clase2_m_v'] += 1
            else:                               # si es superviviente, mujer y de tercera clase
                tercera_clase_v += 1
                superv_m_c3 += 1
                dicc_salida['clase3_m_v'] += 1

    else:                                       # si es muerto
        muertos += 1
        dicc_salida['muertos'] += 1
        if sexo == 'male':                      # si es muerto y hombre
            hombres_m += 1
            dicc_salida['h_m'] += 1

            if clase == primera_clase:          # si es muerto, hombre y de primera clase
                primera_clase_m += 1
                muerto_h_c1 += 1
                dicc_salida['clase1_h_m'] += 1
            elif clase == segunda_clase:        # si es muerto, hombre y de segunda clase
                segunda_clase_m += 1
                muerto_h_c2 += 1
                dicc_salida['clase2_h_m'] += 1
            else:                               # si es muerto, hombre y de tercera clase
                tercera_clase_m += 1
                muerto_h_c3 += 1
                dicc_salida['clase3_h_m'] += 1        
        else:                                   # si es muerto y mujer
            mujeres_m += 1
            dicc_salida['m_m'] += 1

            if clase == primera_clase:          # si es muerto, mujer y de primera clase
                primera_clase_m += 1
                muerto_m_c1 += 1
                dicc_salida['clase1_m_m'] += 1
            elif clase == segunda_clase:        # si es muerto, mujer y de segunda clase
                segunda_clase_m += 1
                muerto_m_c2 += 1
                dicc_salida['clase2_m_m'] += 1
            else:                               # si es muerto, mujer y de tercera clase
                tercera_clase_m += 1
                muerto_m_c3 += 1
                dicc_salida['clase3_m_m'] += 1

 
#print('Numero de muertos TOTALES = ' + str(muertos))
#print(f'Mujeres muertas = {mujeres_m}')
#print(f'Hombres muertos = {hombres_m}')


#print(f'Mujeres vivas = {mujeres_v}')
#print(f'Hombres vivos = {hombres_v}')

print('TOTAL Supervivientes / muertos = ' + str(supervivientes) + ' / ' + str(muertos))
print(f'Total de mujeres supervivientes / mujeres muertas = {mujeres_v} / {mujeres_m}')
print(f'Mujeres de Primera clase supervivientes / muertas =  {superv_m_c1} / {muerto_m_c1}')
print(f'Mujeres de Segunda clase supervivientes / muertas =  {superv_m_c2} / {muerto_m_c2}')
print(f'Mujeres de Tercera clase supervivientes / muertas =  {superv_m_c3} / {muerto_m_c3}')
print('--------------------------------------------------------------------------')
print('TOTAL Supervivientes / muertos = ' + str(supervivientes) + ' / ' + str(muertos))
print(f'Total de hombres supervivientes / hombres muertos = {hombres_v} / {hombres_m}')
print(f'Hombres de Primera clase supervivientes / muertos =  {superv_h_c1} / {muerto_h_c1}')
print(f'Honbres de Segunda clase supervivientes / muertos =  {superv_h_c2} / {muerto_h_c2}')
print(f'Hombres de Tercera clase supervivientes / muertos =  {superv_h_c3} / {muerto_h_c3}')
print('--------------------------------------------------------------------------')
pprint.pprint(dicc_salida)