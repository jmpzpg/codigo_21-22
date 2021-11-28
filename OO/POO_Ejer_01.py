# Ejercicio 1
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

from classPersona import Persona
import re

# ------------------------------------------------

p = Persona('Jose 9anuel', 45, '5007007k')
p.mostrar()
print(p.esMayorDeEdad())