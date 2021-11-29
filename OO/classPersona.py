import re

class Persona():
    __nombre = None
    __edad = None
    __dni = None

    def __init__(self, nombre = None, edad = None, dni = None) -> None:
        self.set_nombre(nombre)
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_dni(self):
        return self.__dni

    def set_nombre(self, nombre):
        if self.__validar_nombre(nombre):
            self.__nombre = nombre
        else:
            print('Por favor, introduzca un nombre de persona válido')

    def set_edad(self, edad):
        if self.__validar_edad(edad):
            self.__edad = edad
        else:
            print('Por favor, introduzca una edad válida (Entre 1 y 120)')

    def set_dni(self, dni):
        if self.__validar_dni(dni):
            self.__dni = dni
        else:
            print('Por favor, introduzca un dni válido (ej: 12345678k)')

    def __validar_nombre(self, nombre):
        cad_limpia = nombre.replace(' ', '')
        if cad_limpia.isalpha():
            return True
        else:
            return False

    def __validar_edad(self, edad):
        if edad.isnumeric() and 0 < int(edad) < 120:
            return True
        else:
            return False
    
    def __validar_dni(self, dni):
        if re.search("[\d]{8}[a-zA-Z]{1}", dni):
            return True
        else:
            return False

    def mostrar(self):
        print(f'Mis datos son:\nNombre: {self.__nombre}\nEdad: {self.get_edad()}\nDNI: {self.get_dni()}')
    
    def esMayorDeEdad(self):
        if int(self.__edad) > 18:
            return True
        else:
            False