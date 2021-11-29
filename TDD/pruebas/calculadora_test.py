from typing_extensions import Self
import unittest
import calculadora

class CalculadoraTest(unittest.TestCase):
    def caracteres_no_numericos_devuelve_error(self):
        respuesta = calculadora.sumar('a,b')
        self.assertEqual(respuesta, 'Error: Carácter NO numérico')