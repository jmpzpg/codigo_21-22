def lee_fichero(nombre):

    try:
        # abrir el archivo
        with open(nombre, 'r') as manejador:
            pass

                        # solo para defndernos de una posible excepcion
    # except:
    #     print('error inesperado')

    
                        # si queremos saber qué excepcion ha sido la que ocurrió
    except Exception as e:
        print(f'error inesperado: {type(e).__name__}')

    else:
        datos = manejador.read()
        print(datos)

# ------------------------

lee_fichero('archivo.txt')
    