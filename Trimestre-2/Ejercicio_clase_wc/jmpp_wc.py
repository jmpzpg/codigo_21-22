from mimetypes import guess_type 

class WC():
    def __init__(self, archivo='') -> None:
        self.__archivo = archivo
        self.__num_lineas = 0
        self.__num_palabras = 0
        self.__num_ocurrencias = {}
        self.__contenido = ' '
        # self.__gestionar_archivo(archivo)

    @property
    def num_lineas(self):
        return self.__num_lineas
    
    @property
    def num_palabras(self):
        return self.__num_palabras

    @property
    def num_ocurrencias(self):
        return self.__num_ocurrencias

    def __gestionar_archivo(self):
        textchars = ''.join(map(chr, [7,8,9,10,12,13,27] + range(0x20, 0x100)))
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
        try:
            with open(self.__archivo, 'r') as manejador:
                texto = manejador.readlines()
                if not is_binary_string(texto):
                    self.__carga_archivo()
        except Exception:
            raise Exception('ERROR: ')

    def __carga_archivo(self):
        pass
    
    def __estadisticas(self):
        self.__rellena_estadisticas()

    def __rellena_estadisticas(self):
       pass
    
    def __validar_archivo(self):
        return guess_type(self.__archivo)[0].split('/')[0] == 'text'

    def abrir_archivo(self):
        try:
            if self.__validar_archivo():
                with open(self.__archivo, 'r') as manejador:
                    contenido = manejador.read()
                    return contenido
        except:
            raise Exception('Archivo no válido')
    
    def contar_lineas(self):
        pass
    def __contar_palabras(self):
        pass
    def __limpiar_cadena(self):
        pass