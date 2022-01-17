"""
Ejercicio 3 :
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando: los tres
atributos, sólo la hora y minuto, o sólo la hora.
Crear además los métodos necesarios para modificar la hora en cualquier momento de forma manual.
Mantenga la integridad de los datos en todo momento definiendo las variables como privadas.

Crear las pruebas unitarias para asegurar el correcto funcionamiento de la clase.

"""


class Tiempo():

    def __init__(self, h=1, m=1, s=1) -> None:
        self.__hora = h
        self.__minuto = m      
    
    @property
    def hora(self):
        return self.__hora
    
    @hora.setter
    def hora(self, h):
        self.__hora = h   

    @property
    def minuto(self):
        return self.__minuto
    
    @minuto.setter
    def minuto(self, m):
        self.__minuto = m

    @property
    def area(self):
        return self.__base * self.__minuto

    @property
    def perimetro(self):
        return 2 * self.__base + 2 * self.__minuto
  
    def __str__(self):
        return (f'Rectángulo de BASE =  {self.__base} y minuto = {self.__minuto}')

# =================================================================================
