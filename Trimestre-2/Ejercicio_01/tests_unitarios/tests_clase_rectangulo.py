import unittest
import Ejer_01_clase_rectangulo

class RectanguloTest(unittest.TestCase):
    def test_caracteres_no_numericos_devuelve_error(self):
        resp = Ejer_01_clase_rectangulo.sumar('a,b')
        self.assertEqual(resp,"Error: Carácter no numérico")
    
    def test_cadena_vacia_devuelve_cero(self):
        resp =  Ejer_01_clase_rectangulo.sumar('')
        self.assertEqual(resp,0)

    def test_un_numero_devuelve_el_numero(self):
        resp = Ejer_01_clase_rectangulo.sumar('1')
        self.assertEqual(resp,1)

    def test_un_caracter_devuelve_el_numero(self):
        respuesta = Ejer_01_clase_rectangulo.sumar('a')
        self.assertEqual(respuesta,"Error: Carácter no numérico")

    def test_dos_numeros_devuelve_suma(self):
        resp = Ejer_01_clase_rectangulo.sumar('2,3')
        self.assertEqual(resp,5)

    def test_numeros_ilimitados_devuelve_suma(self):
        resp = Ejer_01_clase_rectangulo.sumar('1,2,3,4')
        self.assertEqual(resp,10)

    def test_numeros_separados_por_n(self):
        resp = Ejer_01_clase_rectangulo.sumar('1n2n4n5,3')
        self.assertEqual(resp,15)

    def test_barra_barra_punto_coma_devuelve_suma(self):
        resp = Ejer_01_clase_rectangulo.sumar("//;\n1;2")
        self.assertEqual(resp,3)

    def test_valores_negativos_producen_error(self):
        resp = Ejer_01_clase_rectangulo.sumar("3,-6,15,-18,46,33")
        self.assertEqual(resp, "Error: No se admiten números negativos")