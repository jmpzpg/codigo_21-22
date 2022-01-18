"""
Ejercicio 1:
Crear una clase Rectángulo, con atributos base y altura.
Crear también el constructor de la clase y los métodos necesarios para calcular el área y el perímetro.
Crear las pruebas unitarias necesarias para asegurar que funciona correctamente.

"""

class Rectangulo():

    def __init__(self, base=1, altura=1) -> None:
        self.__base = base
        self.__altura = altura      
    
    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, b):
        self.__base = b   

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, a):
        self.__altura = a

    @property
    def area(self):
        return self.__base * self.__altura

    @property
    def perimetro(self):
        return 2 * self.__base + 2 * self.__altura
  
    def __str__(self):
        return (f'Rectángulo de BASE =  {self.__base} y ALTURA = {self.__altura}')

# =================================================================================

rec_1 = Rectangulo()
print(rec_1)

rec_2 = Rectangulo(3,2)
print(rec_2)

print(f'el AREA del rectángulo 1 es de: {rec_1.area}, y el del rectángulo 2 es de: {rec_2.area}')
print(f'el PERIMETRO del rectángulo 1 es de: {rec_1.perimetro}, y el del rectángulo 2 es de: {rec_2.perimetro}')