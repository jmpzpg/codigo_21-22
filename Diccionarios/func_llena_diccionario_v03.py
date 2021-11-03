from typing import Dict
import pprint
#----------------------------------------------
def func_llena_diccionario(hemos_terminado, dic :Dict): 
    #caso recursivo
    if not hemos_terminado:
        entrada_usuario_k = input("Para finalizar pulse ENTER. \nSi desea continuar, por favor, introduzca clave a guardar: ")
        if entrada_usuario_k == '':
            hemos_terminado = True
        else:
            entrada_usuario_v = input("Y ahora, el valor para esa clave: ")
            dic[entrada_usuario_k] = entrada_usuario_v

        func_llena_diccionario(hemos_terminado, dic) 
   
    #caso base
    else:
        print('El usuario ha cancelado la entrada de datos. Los datos actualizados del usuario son:')
#-----------------------------------------------
datos_usuario = {}
hemos_terminado_las_entradas = False
func_llena_diccionario(hemos_terminado_las_entradas, datos_usuario)

pprint.pprint(datos_usuario)
for k,v in datos_usuario.items():
    pprint.pprint(f'{k}: {v}')
