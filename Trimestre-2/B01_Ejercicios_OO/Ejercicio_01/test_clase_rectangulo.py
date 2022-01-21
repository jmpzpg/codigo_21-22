import unittest
from Ejer_01_clase_rectangulo import Rectangulo

class TestClaseRectangulo(unittest.TestCase):
    def test_clase_existe(self):
        r = Rectangulo()
        self.assertNotEqual(r, None)

    def test_constructor_x_defecto_dev_base_1_altura_1(self):
        r = Rectangulo()
        self.assertEqual(r.base, 1)
        self.assertEqual(r.altura, 1)

    def test_constructor_con_parametros(self):
        r = Rectangulo(5,3)
        self.assertEqual(r.base, 5)
        self.assertEqual(r.altura, 3)
    
    def test_base_set_y_get_valor_propiedad(self):
        r = Rectangulo()
        r.base = 8
        self.assertEqual(r.base, 8)
    def test_altura_set_y_get_valor_propiedad(self):
        r = Rectangulo()
        r.altura = 4
        self.assertEqual(r.altura, 4)

    def test_dados_base_altura_calc_area(self):
        r = Rectangulo(5,3)
        self.assertEqual(r.area, 15)

    def test_dados_base_altura_calc_perimetro(self):
        r = Rectangulo(5,3)
        self.assertEqual(r.perimetro, 16)
