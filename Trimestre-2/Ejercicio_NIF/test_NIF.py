import pstats
import unittest
from clase_Nif import Nif

class TestNif(unittest.TestCase):
    def test_clase_existe(self):
        nif = Nif()
        self.assertNotEqual(nif,None)

    def test_constructor_x_defecto_num_cero_y_letra_blanco(self):
        nif = Nif()
        self.assertEqual(nif.numero, 0)
        self.assertEqual(nif.letra, ' ')

    def test_numero_calcula_letra(self):
        nif = Nif(123456)
        self.assertEqual(nif.letra, 'S')