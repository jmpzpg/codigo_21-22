from classPersona import Persona
from classCuenta import Cuenta

class CuentaJoven(Cuenta):
    __bonificacion = 0

    def __init__(self, bonificacion,titular, cantidad=0) -> None:
        super().__init__(titular, cantidad=cantidad)
        #self.__bonificacion = bonificacion
        self.__bonificacion = self.set_bonificacion(bonificacion)   # corregido en clase
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, boni):   # OJO - hay que validar la entrada de la bonificación
        #self.__bonificacion = boni
        if 0 > boni < 0.19:
            return boni
    
    def esTitularValido(self):
        if 18 < self.get_titular().get_edad() < 25:
            return True
        else:
            return False
    
    def retirar(self, cantidad):
        if self.esTitularValido:
            self.set_cantidad -= cantidad

    def mostrar(self):
        return super().mostrar() 