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

    saldo = 100000
    apuesta_base = 50000

    while saldo > 0:
        print(f"\nSaldo: ${saldo:,} COP")
        print(f"Apuesta: ${apuesta_base:,} COP")
        
        if saldo < apuesta_base:
            print("\nTE QUEDASTE SIN PLATA")
            print("Ejecuta el script de nuevo para empezar")
            break

        input("\nPresiona Enter para iniciar la ronda...")

        print("---------------------------------")
        
        baraja, mano_jugador, mano_dealer = iniciar_juego()

        print("\nMano Dealer", end=" ")
        mostrar_mano(mano_dealer, ocultar_primera=True)

        if es_blackjack(mano_jugador):
            print("\nBLACKJACK!")
            saldo += apuesta_base
            print(f"Saldo: ${saldo:,} COP")
            
            continuar = input("\nQuieres seguir jugando? (s/n): ").lower()
            if continuar != 's':
                print(f"\nSaldo final: ${saldo:,} COP")
                break
            continue

        jugador_continua = turno_jugador(baraja, mano_jugador)

        if not jugador_continua:
            saldo -= apuesta_base
            print(f"Saldo: ${saldo:,} COP")
            
            if saldo > 0:
                continuar = input("\nQuieres seguir jugando? (s/n): ").lower()
                if continuar != 's':
                    print(f"\nSaldo final: ${saldo:,} COP")
                    break
            else:
                print("\nTE QUEDASTE SIN PLATA")
                print("Ejecuta el script de nuevo para empezar")
                break
            continue

        dealer_continua = turno_dealer(baraja, mano_dealer)

        print("\n=== RESULT ===")
        if not dealer_continua:
            print("SE PASO EL DEALER, GANASTE")
            saldo += apuesta_base
        elif es_empate(mano_jugador, mano_dealer):
            print("eeempate")
            # En empate no se gana ni se pierde
        elif jugador_gana(mano_jugador, mano_dealer):
            print("TU ERE UN GANADOR")
            saldo += apuesta_base
        else:
            print("gano el dealer :(")
            saldo -= apuesta_base

        print(f"Saldo: ${saldo:,} COP")

        if saldo > 0:
            continuar = input("\nQuieres seguir jugando? (s/n): ").lower()
            if continuar != 's':
                print(f"\nSaldo final: ${saldo:,} COP")
                break
        else:
            print("\nTE QUEDASTE SIN PLATA")
            print("Ejecuta el script de nuevo para empezar")


if __name__ == "__main__":
    jugar_blackjack()