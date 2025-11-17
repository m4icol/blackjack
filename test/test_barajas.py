from barajas import crear_baraja, mezclar_baraja, palos, valores

def test_crear_baraja_tiene_52_cartas():
    baraja = crear_baraja()
    assert len(baraja) == 52

def test_crear_baraja_contiene_todos_los_palos():
    baraja = crear_baraja()

    palos_en_baraja = []
    for carta in baraja:
        palo = carta[1]
        if palo not in palos_en_baraja:
            palos_en_baraja.append(palo)

    assert sorted(palos_en_baraja) == sorted(palos)



def test_crear_baraja_contiene_todos_los_valores():
    baraja = crear_baraja()

    valores_en_baraja = []
    for carta in baraja:
        valor = carta[0]
        if valor not in valores_en_baraja:
            valores_en_baraja.append(valor)

    assert sorted(valores_en_baraja) == sorted(valores.keys())



def test_mezclar_baraja_cambia_orden():
    baraja1 = crear_baraja()
    baraja2 = crear_baraja()
    baraja_mezclada = mezclar_baraja(baraja2)
    assert baraja1 != baraja_mezclada

def test_mezclar_baraja_mantiene_52_cartas():
    baraja = crear_baraja()
    baraja_mezclada = mezclar_baraja(baraja)
    assert len(baraja_mezclada) == 52