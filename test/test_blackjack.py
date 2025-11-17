import pytest
from turnos import es_blackjack

@pytest.fixture
def mano_blackjack_as_rey():
    return [('A', '♥️'), ('K', '♦️')]

@pytest.fixture
def mano_blackjack_as_diez():
    return [('A', '♠️'), ('10', '♣️')]

@pytest.mark.parametrize("mano", [
    [('A', '♥️'), ('Q', '♦️')],
    [('A', '♠️'), ('J', '♣️')],
    [('A', '♦️'), ('K', '♠️')],
    [('A', '♣️'), ('10', '♥️')],
])
def test_es_blackjack_con_todas_combinaciones(mano):
    assert es_blackjack(mano) == True
