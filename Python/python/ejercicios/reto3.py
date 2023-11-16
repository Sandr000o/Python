'''
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''
def mostrar_puntuacion(p1, p2):
    puntuaciones = ["Love", 15, 30, 40]

    if p1 == p2:
        if p1 < 3:
            print(f"{puntuaciones[p1]} - All")
        elif p1 == 3:
            print("Deuce")
        elif p1 > 3:
            print("Ventaja P1")
    elif p1 > 3 or p2 > 3:
        if p1 > p2:
            print("Ha ganado el P1")
        else:
            print("Ha ganado el P2")
    else:
        print(f"{puntuaciones[p1]} - {puntuaciones[p2]}")


def juego_de_tenis(secuencia):
    puntuacion_p1 = 0
    puntuacion_p2 = 0

    for punto in secuencia:
        if punto == "P1":
            puntuacion_p1 += 1
        elif punto == "P2":
            puntuacion_p2 += 1

        mostrar_puntuacion(puntuacion_p1, puntuacion_p2)


# Ejemplo de uso
secuencia_juego = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
juego_de_tenis(secuencia_juego)
