# Jose Manuel Perez Puig

class Persona():
   
    def __init__(self, nombre = 'nombre', apellidos = 'apellidos',  edad = 'edad', dni = 'DNI') -> None:
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__dni = dni
# ---------------------------------------------------    
    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_edad(self):
        return self.__edad

    def get_dni(self):
        return self.__dni
# ---------------------------------------------------
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellidos(self, ape):
        self.__apellidos = ape

    def set_edad(self, edad):
        self.__edad = edad

    def set_dni(self, dni):
        self.__dni = dni
# ---------------------------------------------------
    def __str__(self) -> str:
        return f'Nombre: {self.__nombre} -- Apellidos: {self.__apellidos} -- Edad: {self.__edad} -- DNI: {self.__dni}'
    
# ==================================================

# Líneas comentadas para que no me molesten en el ejercicio 3

#p = Persona('JM','p',20,'12345678K')
#print(p)