import unittest
from clase_simulador_juego import Simulador

class TestClaseSimulador(unittest.TestCase):
    def test_existencia(self):
        partida = Simulador()
        self.assertNotEqual(partida, None)

    def test_constructor_x_defecto_tiradas_a_cero_ganador_cadvacia(self):
        partida = Simulador()
        self.assertEqual(partida.num_tiradas, 0)
        self.assertEqual(partida.ganador, '')

    def test_iniciar_partida_dev_dic_con_ganador_y_tiradas(self):
        partida = Simulador()
        fin = partida.iniciar_partida()
        self.assertEqual(fin['ganador'], partida.ganador)
        self.assertEqual(fin['tiradas'], partida.num_tiradas)
