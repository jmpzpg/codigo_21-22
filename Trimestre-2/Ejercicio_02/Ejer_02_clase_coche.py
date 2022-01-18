"""
Ejercicio 2:
Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el modelo, el número de puertas y la matrícula.
Crear el constructor del coche, así como los métodos que considere necesarios.
Crear las pruebas unitarias necesarias para comprobar que se pueden establecer y consultar los valores de los atributos.

"""

class Coche():

    def __init__(self, marca='', modelo='', color='', num_puertas='', matricula='') -> None:
        self.__marca = marca
        self.__modelo = modelo  
        self.__color = color
        self.__num_puertas = str(num_puertas) 
        self.__matricula = matricula    
    
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, mar):
        self.__marca = mar   

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, mod):
        self.__modelo = mod

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, col):
        self.__color = col   

    @property
    def num_puertas(self):
        return self.__num_puertas
    @num_puertas.setter
    def num_puertas(self, num):
        self.__num_puertas = str(num)

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, mat):
        self.__matricula = mat
  
    def __str__(self):
        return (f'---------------------------------\nLas características del COCHE son: \n---------------------------------\n   Marca -------------> {self.__marca}\n   Modelo ------------> {self.__modelo}\n   Color -------------> {self.__color}\n   Número de puertas -> {self.__num_puertas}\n   Matrícula ---------> {self.__matricula}\n. . . . . . . . . . . . . . . . . ')

# =================================================================================

c1 = Coche()
print(c1)
c2 = Coche('Renault','Clio','azul otomano',5,'9001-LHV')
print(c2)
c1.num_puertas = 4
c1.color = 'atardecer en Barbados'
c1.matricula = '2022-GJA'
c1.marca = 'Seat'
print(c1)