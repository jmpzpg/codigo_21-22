# Ejercicio Pagina-45:
"""
Dada una cadena de texto, convertir cada carcater a su codigo ASCII.
Con eso creamos un numero formado por todos los codigos unidos, que llamaremos total_1.
Cambiar todos los numeros '7' por el numero '1', al que llamaremos total_2
Devolver la resta de total_1 - total_2

"""
 

def convertir_a_ascii_y_restarlos(cadena):
    total_1 = total_2 = ''

    for elem in cadena:
        total_1 += str(ord(elem))
    total_2 = total_1.replace('7','1')
    
    print(total_1)
    print(total_2)

    return int(total_1) - int(total_2)
# -------------------------------------

print(convertir_a_ascii_y_restarlos('CCC'))