

class Racional():
    __numerador = 0
    __denominador = 1

    def __init__(self, numerador=0, denominador=1) -> None:
        self.__numerador = numerador
        #self.__denominador = denominador
        self.set_denominador(denominador)

    def __str__(self) -> str:
        return print(self.__numerador, ' / ', self.__denominador)
    
    def get_numerador(self):
        return self.__numerador

    def get_denominador(self):
        return self.__denominador

    def set_numerador(self, num):
        self.__numerador = num

    def set_denominador(self, denom): # solo si distinto de cero
        if denom != 0:
            self.__denominador = denom

    def sumar(self, r):
        return Racional(self.get_numerador()*r.get_denominador() + self.get_denominador()*r.get_numerador(), self.get_denominador()*r.get_denominador())

    def restar(self, r):
        return Racional(self.get_numerador()*r.get_denominador() - self.get_denominador()*r.get_numerador(), self.get_denominador()*r.get_denominador())

    def multiplicar(self, r):
        return Racional(self.__numerador * r.get_numerador(), self.__denominador * r.get_denominador())

    def dividir(self, r):
        return Racional(self.__numerador * r.get_denominador(), self.__denominador * r.get_numerador())
    
    
# ----------------------------------------------------------------------------

num_racional_1 = Racional(3,4)
print(f'El numero racional 1 es: {num_racional_1.get_numerador()} / {num_racional_1.get_denominador()}')
num_racional_2 = Racional(1,4)
print(f'El numero racional 2 es: {num_racional_2.get_numerador()} / {num_racional_2.get_denominador()}')
numero_multiplicacion = num_racional_1.multiplicar(num_racional_2)
print(f'El resultado de la multiplicación es: {numero_multiplicacion.get_numerador()} / {numero_multiplicacion.get_denominador()}')
numero_suma = num_racional_1.sumar(num_racional_2)
print(f'El resultado de la suma es: {numero_suma.get_numerador()} / {numero_suma.get_denominador()}')
numero_resta = num_racional_1.restar(num_racional_2)
print(f'El resultado de la resta es: {numero_resta.get_numerador()} / {numero_resta.get_denominador()}')
numero_division = num_racional_1.dividir(num_racional_2)
print(f'El resultado de la división es: {numero_division.get_numerador()} / {numero_division.get_denominador()}')
numero_division.__str__()






# ---------------------------------------------------------



""" def mcd2(x, y):
        mayor = max(x, y)
        menor = min(x, y)
        if ((x and y) == 0):
            menor = mayor
        else:
            r = mayor % menor
            while r != 0:
                mayor = r
                r = menor % r
                menor = mayor
        return math.fabs(menor)
    
    def mcd(*n):
        numeros = list(n)
        resultado = mcd2(numeros[0], numeros[1])
        if len(numeros) > 2:
            for n in numeros[2:]:
                resultado = mcd2(resultado, n)
        return math.fabs(resultado)

    def mcm(*n):
        numeros = list(n)
        if np.prod(numeros) != 0:
            resultado = np.prod(numeros)/mcd(*n)**(len(numeros) - 1)
        else:
            resultado = float('nan')
        return math.fabs(resultado) """