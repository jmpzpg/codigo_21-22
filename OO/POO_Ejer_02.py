# Ejercicio 2
# Crea una clase llamada **Cuenta** que tendrá los siguientes atributos: 
# - titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad 
# es opcional. Construye los siguientes métodos para la clase:

# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, 
# sólo ingresando o retirando dinero.
# - mostrar(): Muestra los datos de la cuenta.
# - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
# no se hará nada.
# - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

from classPersona import Persona
from classCuenta import Cuenta

# ---------------------------------------------------------

cliente01 = Persona('Roberto', 25, '12345678k')
cliente02 = Persona('Isabel María', 30, '33444555L')
cuenta01 = Cuenta(cliente01, 100)
print(cuenta01.mostrar())
cuenta02 = Cuenta(cliente02)
print(cuenta02.mostrar())
cuenta02.ingresar(55)
print(cuenta02.mostrar())