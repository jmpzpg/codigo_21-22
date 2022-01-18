import unittest
from Ejer_03_clase_tiempo import Tiempo

class TestClaseTiempo(unittest.TestCase):
    def test_primero(self):
        pass
    
    def test_clase_existe(self):
        t = Tiempo()
        self.assertNotEqual(t, None)

    def test_constructor_x_defecto_hora_cerocero_minuto_cerocero_segundo_cerocero(self):
        t = Tiempo()
        self.assertEqual(t.hora,'00')
        self.assertEqual(t.minuto, '00')
        self.assertEqual(t.segundo, '00')
    
    def test_constructor_con_cadenas_h_m_s(self):
        t = Tiempo('08','30','55')
        self.assertEqual(t.hora,'08')
        self.assertEqual(t.minuto, '30')
        self.assertEqual(t.segundo, '55')
    def test_constructor_con_enteros_h_m_s(self):
        t = Tiempo(8,30,55)
        self.assertEqual(t.hora,'08')
        self.assertEqual(t.minuto, '30')
        self.assertEqual(t.segundo, '55')

    def test_constructor_con_cadenas_h_m(self):
        t = Tiempo('10','45')
        self.assertEqual(t.hora,'10')
        self.assertEqual(t.minuto, '45')
        self.assertEqual(t.segundo, '00')
    def test_constructor_con_enteros_h_m(self):
        t = Tiempo(10,45)
        self.assertEqual(t.hora,'10')
        self.assertEqual(t.minuto, '45')
        self.assertEqual(t.segundo, '00')

    def test_constructor_con_cadena_h(self):
        t = Tiempo('13')
        self.assertEqual(t.hora,'13')
        self.assertEqual(t.minuto, '00')
        self.assertEqual(t.segundo, '00')
    def test_constructor_con_entero_h(self):
        t = Tiempo(13)
        self.assertEqual(t.hora,'13')
        self.assertEqual(t.minuto, '00')
        self.assertEqual(t.segundo, '00')

    def test_hora_setter(self):
        t = Tiempo()
        t.hora = 14
        t.minuto = 15
        t.segundo = 16
        self.assertEqual(t.hora, '14')
        self.assertEqual(t.minuto, '15')
        self.assertEqual(t.segundo, '16')

    def test_imprimir_tiempo(self):
        t = Tiempo(12,35,42)
        self.assertEqual(t.__str__(), 'Tiempo guardado = 12:35:42')