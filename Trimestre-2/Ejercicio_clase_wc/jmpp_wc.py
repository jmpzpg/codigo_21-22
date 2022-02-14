class WC():
    def __init__(self, archivo='') -> None:
        self.__num_lineas = 0
        self.__num_palabras = 0
        self.__num_ocurrencias = {}
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

    def __gestionar_archivo(self, archivo):
        textchars = ''.join(map(chr, [7,8,9,10,12,13,27] + range(0x20, 0x100)))
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
        try:
            with open(archivo, 'r') as manejador:
                texto = manejador.readlines()
                if not is_binary_string(texto):
                    self.__carga_archivo(archivo)
        except Exception:
            raise Exception('ERROR: ')

    def __carga_archivo(self, archivo):
        pass
    
    def __estadisticas(self, archivo):
        self.__rellena_estadisticas()

    def __rellena_estadisticas(self):
       pass
    