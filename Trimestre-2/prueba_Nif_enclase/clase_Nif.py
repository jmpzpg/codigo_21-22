class Nif():
    dic_letras = {0:'T',1:'R',2:'W',3:'A',4:'G',5:'M',6:'Y',7:'F',8:'P',9:'D',10:'X',11:'B',
                12:'N',13:'J',14:'Z',15:'S',16:'Q',17:'V',18:'H',19:'L',20:'C',21:'K',22:'E'}
    
    def __init__(self, numero=0, letra=' ') -> None:
        self.__numero = numero
        if not numero:
            self.__letra = letra
        else:
            self.__nif_con_datos(numero)
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, num):
        #self.__numero = num
        self.__init__(num)

    @property
    def letra(self):
        return self.__letra
    
    """ @letra.setter
    def letra(self, letra):
        self.__letra = letra """

    @property
    def leer(self):
        numero = int(input('Introduce tu numero de NIF, sin la letra: '))
        self.__init__(numero)

    def __calc_letra(self, numero):
        resto = numero % 23
        return self.dic_letras[resto]

    def __nif_con_datos(self, num):
        self.__letra = self.__calc_letra(num)
    
    def __str__(self):
        return (f'Tu número de NIF es: {self.__numero}-{self.__letra}')

# =================================================================================
