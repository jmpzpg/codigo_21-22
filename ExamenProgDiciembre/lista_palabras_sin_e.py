# Jose Manuel Perez Puig

def func_lista_palabras_sin_e(txt):
    lista_salida = [] 
    with open(txt, 'r') as manejador:
        elementos = manejador.readlines()
        for elem in elementos:
            if elem.find('e') == -1:                # Si no aparece el caracter e en la palabra
                lista_salida.append(elem[:-1])
    return lista_salida  

# ---------------------------------------------------

# Usamos la técnica de inyección de dependencias y declaramos los componentes de la ruta y del txt aquí, fuera de la función.
ruta = '/home/jmpp/codigo/codigo_21-22/ExamenProgDiciembre/'
archivo = 'palabras.txt'
print(func_lista_palabras_sin_e(ruta + archivo)) 
