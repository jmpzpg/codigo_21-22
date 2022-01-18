"""
Ejercicio 3 :
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando: los tres
atributos, sólo la hora y minuto, o sólo la hora.
Crear además los métodos necesarios para modificar la hora en cualquier momento de forma manual.
Mantenga la integridad de los datos en todo momento definiendo las variables como privadas.

Crear las pruebas unitarias para asegurar el correcto funcionamiento de la clase.

"""


class Tiempo():

    def __init__(self, h='00', m='00', s='00') -> None:
        self.__hora = self.__tiempo_a_txt(h)
        self.__minuto = self.__tiempo_a_txt(m)
        self.__segundo = self.__tiempo_a_txt(s)
    
    @property
    def hora(self):
        return self.__hora
    @hora.setter
    def hora(self, h):
        self.__hora = self.__tiempo_a_txt(h)  

    @property
    def minuto(self):
        return self.__minuto
    @minuto.setter
    def minuto(self, m):
        self.__minuto = self.__tiempo_a_txt(m)

    @property
    def segundo(self):
        return self.__segundo
    @segundo.setter
    def segundo(self,s):
        self.__segundo = self.__tiempo_a_txt(s)

    def __tiempo_a_txt(self, t):
        t_cad = str(t)
        if len(t_cad) == 2:
            return t_cad
        else:
            return '0'+ t_cad
    
  
    def __str__(self):
        return (f'La Hora es: {self.__hora}:{self.__minuto}:{self.__segundo}')

# =================================================================================

t1 = Tiempo()
t2 = Tiempo(20,00,00)
t3 = Tiempo(23,55)
print(t1)
print(t2)
print(t3)
