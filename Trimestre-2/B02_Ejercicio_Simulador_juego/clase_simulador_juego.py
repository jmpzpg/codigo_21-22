from random import randrange

class Simulador():
    
    def __init__(self) -> None:
        self.num_tiradas = 0
        self.ganador = ''
    
    def iniciar_partida(self):
        hay_ganador = False
        jugador1_puntos = Jugador2_puntos = 0
        num_tirada = 0
        salida = {'ganador': '', 'tiradas': 0}
        while not hay_ganador:
            num_tirada += 1
            jugador1_puntos += randrange(1,6)
            Jugador2_puntos += randrange(1,6)
            print(f'Tirada: {num_tirada}\n    Jugador1: {jugador1_puntos} puntos\n    Jugador2: {Jugador2_puntos} puntos')
            if jugador1_puntos >= 100 and Jugador2_puntos >= 100:
                salida['ganador'] = '¡¡ Los jugadores 1 y 2 han empatado !!'
                hay_ganador = True
                break
            elif jugador1_puntos >= 100:
                salida['ganador'] = '¡¡ El jugador 1 ha ganado !!'
                hay_ganador = True
            elif Jugador2_puntos >= 100:
                salida['ganador'] = '¡¡ El jugador 2 ha ganado !!'
                hay_ganador = True
        if hay_ganador:
            salida['tiradas'] = num_tirada
            self.num_tiradas = num_tirada
            self.ganador = salida['ganador']
        return salida
         
# =================================================================

partida1 = Simulador()
resumen = partida1.iniciar_partida()
print(f'Partida acabada en {partida1.num_tiradas} tiradas y {partida1.ganador}')
print('La partida acabó en ' + str(resumen['tiradas']) + ' tiradas y ' + resumen['ganador'])