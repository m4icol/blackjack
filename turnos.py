from barajas import calcular_valor, mostrar_mano, repartir_carta


def jugador_gana(mano_jugador, mano_dealer):
    valor_jugador = calcular_valor(mano_jugador)
    valor_dealer = calcular_valor(mano_dealer)

    if valor_jugador > 21:
        return False
    if valor_dealer > 21:
        return True
    return valor_jugador > valor_dealer

def es_blackjack(mano):
    return len(mano) == 2 and calcular_valor(mano) == 21

def es_empate(mano_jugador, mano_dealer):
    return calcular_valor(mano_jugador) == calcular_valor(mano_dealer)

def turno_jugador(baraja, mano_jugador):
    while True:
        print("\nMano:", end=" ")
        mostrar_mano(mano_jugador)
        print(f"Valor: {calcular_valor(mano_jugador)}")

        if calcular_valor(mano_jugador) > 21:
            print("Te pasaste, perdiste :(")
            return False

        if calcular_valor(mano_jugador) == 21:
            print("GANASTE POR 21")
            return True

        accion = input("Sigues (s) o te Quedas (q)? ").lower()

        if accion == 's':
            mano_jugador.append(repartir_carta(baraja))
        elif accion == 'q':
            return True
        else:
            print("Opcion no valida, digite la letra 's' o 'q'")

def turno_dealer(baraja, mano_dealer):
    print("\nTurno del Dealer:")
    while calcular_valor(mano_dealer) < 17:
        print("Mano:", end=" ")
        mostrar_mano(mano_dealer)
        print(f"Valor: {calcular_valor(mano_dealer)}")

        mano_dealer.append(repartir_carta(baraja))

    print("\nMano final del Dealer:", end=" ")
    mostrar_mano(mano_dealer)
    print(f"Valor: {calcular_valor(mano_dealer)}")

    return calcular_valor(mano_dealer) <= 21