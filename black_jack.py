from barajas import crear_baraja, mezclar_baraja, mostrar_mano, repartir_carta
from turnos import es_blackjack, es_empate, jugador_gana, turno_dealer, turno_jugador

def iniciar_juego():
    baraja = mezclar_baraja(crear_baraja())
    mano_jugador = [repartir_carta(baraja), repartir_carta(baraja)]
    mano_dealer = [repartir_carta(baraja), repartir_carta(baraja)]
    return baraja, mano_jugador, mano_dealer

def jugar_blackjack():
    print("==================")
    print("=== BLACK JACK ===")
    print("==================")

    saldo = 100000
    apuesta_base = 50000

    while saldo > 0:
        print(f"\nSaldo: ${saldo:,}")
        print(f"Apuesta: ${apuesta_base:,}")

        if saldo < apuesta_base:
            print("No tienes suficiente dinero para seguir jugando.")
            break

        input("\nPresiona Enter para iniciar la ronda...")

        baraja, mano_jugador, mano_dealer = iniciar_juego()

        print("\nMano Dealer:", end=" ")
        mostrar_mano(mano_dealer, ocultar_primera=True)

        if es_blackjack(mano_jugador):
            print("\nBLACKJACK! Ganaste!")
            saldo += apuesta_base
            continue

        if not turno_jugador(baraja, mano_jugador):
            saldo -= apuesta_base
            continue

        if not turno_dealer(baraja, mano_dealer):
            saldo += apuesta_base
            continue

        if es_empate(mano_jugador, mano_dealer):
            print("\nEmpate! No pierdes ni ganas.")
        elif jugador_gana(mano_jugador, mano_dealer):
            print("\nGanaste!")
            saldo += apuesta_base
        else:
            print("\nPerdiste :(")
            saldo -= apuesta_base

    print(f"\nSaldo final: ${saldo:,}")

if __name__ == "__main__":
    jugar_blackjack()
