import pytest
from black_jack import iniciar_juego

@pytest.fixture
def juego_inicial():
    return iniciar_juego()

def test_jugador_recibe_dos_cartas(juego_inicial):
    baraja, mano_jugador, mano_dealer = juego_inicial
    assert len(mano_jugador) == 2

def test_dealer_recibe_dos_cartas(juego_inicial):
    baraja, mano_jugador, mano_dealer = juego_inicial
    assert len(mano_dealer) == 2

def test_baraja_disminuye_despues_reparto(juego_inicial):
    baraja, mano_jugador, mano_dealer = juego_inicial
    assert len(baraja) == 48

def test_cartas_repartidas_son_diferentes(juego_inicial):
    baraja, mano_jugador, mano_dealer = juego_inicial
    todas_cartas = mano_jugador + mano_dealer
    assert len(todas_cartas) == 4

@pytest.mark.parametrize("iteracion", range(5))
def test_multiples_juegos_inicializan_correctamente(iteracion):
    baraja, mano_jugador, mano_dealer = iniciar_juego()
    assert len(mano_jugador) == 2
    assert len(mano_dealer) == 2
    assert len(baraja) == 48