import unittest
import simulador_juego_sencillo

class TestSimuladorJuegoSencillo(unittest.TestCase):

    resp = simulador_juego_sencillo.simulador_juego()
    
    def test_los_jugadores_empatan(self):
        self.assertEqual(self.resp, '¡¡ Los jugadores 1 y 2 han empatado !! \n GAME OVER') 

    def test_gana_el_jugador1(self):
        self.assertEqual(self.resp, '¡¡ El jugador 1 ha ganado !! \n GAME OVER')

    def test_gana_el_jugador2(self):
        self.assertEqual(self.resp, '¡¡ El jugador 2 ha ganado !! \n GAME OVER')