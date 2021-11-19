from typing import Dict
import pprint
DATOS = 4

hemos_terminado_entrada = False
datos_usuario = {'Nombre': None, 'Apellidos': None, 'Fecha de Nacimiento': None, 'Teléfono': None}
lista_claves = list(datos_usuario.keys()) 
lista_diccionarios_usuarios = []
while not hemos_terminado_entrada:
    
    for i in range(DATOS):
        datos_usuario[lista_claves[i]] = input(f"Por favor, introduzca {lista_claves[i]} a guardar: ")
    bandera = input("Para finalizar pulse ENTER. \nSi desea continuar, por favor, pulse la letra 'c': ")
    lista_diccionarios_usuarios.append(datos_usuario)

    if bandera == '':
        hemos_terminado_entrada = True
    else:
        pass

print('--------------------------------')
cont = 1
for i in lista_diccionarios_usuarios:
    
    print(f'------ Usuario número {cont} ------')
    print('--------------------------------')
    for k,v in i.items():
        pprint.pprint(f'{k}: {v}')
    print('--------------------------------')
    cont += 1