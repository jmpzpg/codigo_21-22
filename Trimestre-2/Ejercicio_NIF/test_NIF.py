import unittest
from clase_NIF import Nif 

class TestNif(unittest.TestCase):
    def test_clase_existe(self):
        resp = Nif()
        self.assertNotEqual(resp,None)

    def test_constructor_x_defecto_num_cero_y_letra_blanco(self):
        resp = Nif()
        self.assertEqual(resp.numero, 0)
    