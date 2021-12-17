# Jose Manuel Perez Puig

from clase_persona import Persona

def func_lista_de_personas():
    lista_personas = []
    hemos_terminado = False

    while not hemos_terminado:
        print('Introduce los datos de la persona. ** N para terminar **')
        v_nom = input('Introduce el nombre: ')
        v_ape = input('Introduce los apellidos: ')
        v_edad = input('Introduce la edad: ')
        v_dni = input('Introduce el DNI: ')
        p = Persona(v_nom, v_ape, v_edad, v_dni)
        lista_personas.append(p)
        resp = input('¿Deseas continuar s/n?')
        if resp.upper() == 'N':
            hemos_terminado = True

    return lista_personas

# ---------------------------------------------------------------------

lista = func_lista_de_personas()
for elem in lista:
    print(elem.__str__())