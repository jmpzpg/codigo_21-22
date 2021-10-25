def es_palindromo(texto_candidato):
    cadena = (str(texto_candidato)).strip()
    """lista = cadena.split()
    lista_invertida = lista.reverse()
     for i in range(len(lista)):
        directo = lista[i]
        inverso = lista_invertida[i]
        if  directo == inverso:
            es_cierto = True
        else:
            None """

    """ cadena_sin_espacios = cadena.split()
    lista = []
    a = len(cadena_sin_espacios)
    for i in cadena_sin_espacios:
        lista[i] = i. """

def limpiar_cadena(texto_candidato):
    cadena = texto_candidato
    cad_may = cadena.upper()
    cad_may = cad_may.replace(' ','')
    cad_may = cad_may.replace(',','')
    cad_may = cad_may.replace('.','')
    cad_may = cad_may.replace(';','')
    cad_may = cad_may.replace(':','')
    cad_may = cad_may.replace('Á','A')
    cad_may = cad_may.replace('É','E')
    cad_may = cad_may.replace('Í','I')
    cad_may = cad_may.replace('Ó','O')
    cad_may = cad_may.replace('Ú','U')
    return cad_may
    
salida = ''
texto_candidato = 'SOMETAMOS ó, mATEMOS'
es_cierto = False
cad = limpiar_cadena(texto_candidato)
for x in cad:
    salida = x.upper() + salida

if salida == cad:
    return True
else:
    return False




respuesta = es_palindromo(cad)
if respuesta:
    print('el texto es un palindromo')
else:
    print('El texto NO es un palindromo')
