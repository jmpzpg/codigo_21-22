def decorador_suma(funcion_que_suma):

    def envoltura(numeros_a_sumar):

        if not type(numeros_a_sumar) == list:
            return funcion_que_suma(preparar_numeros_a_sumar(numeros_a_sumar)) 
        else:
            return funcion_que_suma(numeros_a_sumar) 

    return envoltura
    
# -------------------------------------------------

def preparar_numeros_a_sumar(nums):
    lista_de_numeros = []
    for elem in nums:
        if elem != ',':
            lista_de_numeros.append(int(elem))
    return lista_de_numeros

# -------------------------------------------------

@decorador_suma
def sumar(numeros_a_sumar):
    return sum(numeros_a_sumar)

# -------------------------------------------------

numeros_en_cadena = "1,2,3,4"
numeros_en_lista = [1,2,3,4,5]

print(sumar(numeros_en_cadena))
print(sumar(numeros_en_lista))