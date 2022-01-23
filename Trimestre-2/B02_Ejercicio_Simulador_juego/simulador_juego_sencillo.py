from random import randrange

def simulador_juego():
    hay_ganador = False
    jugador1_puntos = Jugador2_puntos = 0
    num_tirada = 0
    while not hay_ganador:
        num_tirada += 1
        jugador1_puntos += randrange(1,6)
        Jugador2_puntos += randrange(1,6)
        print(f'Tirada: {num_tirada}\n    Jugador1: {jugador1_puntos} puntos\n    Jugador2: {Jugador2_puntos} puntos')
        if jugador1_puntos >= 100 and Jugador2_puntos >= 100:
            salida = '¡¡ Los jugadores 1 y 2 han empatado !!'
            break
        elif jugador1_puntos >= 100:
            salida = '¡¡ El jugador 1 ha ganado !!'
            hay_ganador = True
        elif Jugador2_puntos >= 100:
            salida = '¡¡ El jugador 2 ha ganado !!'
            hay_ganador = True
        

    return f'{salida} \n GAME OVER'

    # ============================================================

print(simulador_juego())
