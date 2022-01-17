import unittest
from clase_Nif import Nif

class TestClaseNif(unittest.TestCase):
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
        nif = Nif(75541171)
        self.assertEqual(nif.letra, 'V')

    def test_numero_setter_calcula_letra(self):
        nif = Nif()
        nif.numero = 20000000
        self.assertEqual(nif.letra,'M')

    def test_leer_y_print_nif(self):
        nif = Nif()
        nif.numero = 20000000
        self.assertEqual(nif.__str__(), 'Tu número de NIF es: 20000000-M')