from classPersona import Persona

class Cuenta():
    #__titular = Persona
    #__cantidad = 0.0

    def __init__(self, titular, cantidad = 0.00) -> None:
        self.__titular = titular
        self.__cantidad = cantidad
    
    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def mostrar(self):
        return (f'Los datos de la cuenta son:\nNombre del titular de la cuenta: {self.__titular.get_nombre()}\nSaldo de la cuenta: {self.get_cantidad()}')

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad