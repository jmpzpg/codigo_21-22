def decorador_suma(funcion_que_suma):

    def envoltura(*args):

        if not type(args) == list:
            return funcion_que_suma(preparar_numeros_a_sumar(args)) 
        else:
            return funcion_que_suma(args) 

    return envoltura
    
# -------------------------------------------------

def preparar_numeros_a_sumar(*args):
    lista_de_numeros = []
    print(args(0))
    cadena = args(0)
    for elem in cadena:
        if elem != ',':
            lista_de_numeros.append(int(elem))
    return lista_de_numeros

# -------------------------------------------------

def gestionar_tupla(*args):
    cadena = list(args(0))





@decorador_suma
def sumar(*args):
    return sum(args)

# -------------------------------------------------

numeros_en_cadena = "1,2,3,4"
numeros_en_lista = [1,2,3,4,5]

print(sumar(numeros_en_cadena))
#print(sumar(numeros_en_lista))