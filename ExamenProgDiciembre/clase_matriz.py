# Jose Manuel Perez Puig

class Matriz():
    __elem = '0'     # Los elementos que formarán la matriz, en este caso será el carácter cero

    def __init__(self, ancho = 1, alto = 1) -> None:
        self.__ancho = ancho
        self.__alto = alto

# ---------------------------------------------------    
    def get_ancho(self):
        return self.__ancho

    def get_alto(self):
        return self.__alto

# ---------------------------------------------------
    def set_ancho(self, ancho):
        self.__ancho = ancho

    def set_alto(self, alto):
        self.__alto = alto

# ---------------------------------------------------

    def __str__(self) -> str:
        return self.__generar_mat()


    def __generar_mat(self):    # Nos va montando la matriz según sea su alto
        m = ''
        for i in range(self.__alto):
            m += f'{self.__dame_fila()}\n'

        return m

    def __dame_fila(self):      # Nos va montando cada fila de la matriz según sea su ancho
        fila = ''
        for i in range(self.__ancho):
            fila += f' {self.__elem} '
        return fila


# ===================================================

m = Matriz(3,3)
print(m.__str__())