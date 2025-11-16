from barajas import crear_baraja, mezclar_baraja, mostrar_mano, repartir_carta
from turnos import es_blackjack, es_empate, jugador_gana, turno_dealer, turno_jugador


def iniciar_juego():
    baraja = crear_baraja()
    baraja = mezclar_baraja(baraja)

    mano_jugador = []
    mano_dealer = []

    mano_jugador.append(repartir_carta(baraja))
    mano_dealer.append(repartir_carta(baraja))
    mano_jugador.append(repartir_carta(baraja))
    mano_dealer.append(repartir_carta(baraja))

    return baraja, mano_jugador, mano_dealer

def jugar_blackjack():
    print("==================\n")
    print("=== BLACK JACK ===\n")
    print("==================\n")

    baraja, mano_jugador, mano_dealer = iniciar_juego()

    print("Mano Dealer", end=" ")
    mostrar_mano(mano_dealer, ocultar_primera=True)

    if es_blackjack(mano_jugador):
        print("\nBLACKJACK!")
        return

    jugador_continua = turno_jugador(baraja, mano_jugador)

    if not jugador_continua:
        return

    dealer_continua = turno_dealer(baraja, mano_dealer)

    print("\n=== RESULT ===")
    if not dealer_continua:
        print("SE PASO EL DEALER, GANASTE")
    elif es_empate(mano_jugador, mano_dealer):
        print("eeempate")
    elif jugador_gana(mano_jugador, mano_dealer):
        print("TU ERE UN GANADOR")
    else:
        print("gano el dealer :(")
