import pytest
from barajas import calcular_valor

@pytest.mark.parametrize("mano,valor_esperado", [
    ([('5', '♥️'), ('7', '♦️')], 12),
    ([('2', '♠️'), ('3', '♣️')], 5),
    ([('10', '♥️'), ('10', '♦️')], 20),
])
def test_calcular_valor_cartas_numericas(mano, valor_esperado):
    assert calcular_valor(mano) == valor_esperado



@pytest.mark.parametrize("mano,valor_esperado", [
    ([('K', '♠️'), ('Q', '♣️')], 20),
    ([('J', '♥️'), ('K', '♦️')], 20),
    ([('Q', '♠️'), ('J', '♣️'), ('A', '♥️')], 21),
])
def test_calcular_valor_figuras(mano, valor_esperado):
    assert calcular_valor(mano) == valor_esperado



def test_calcular_valor_as_como_11():
    mano = [('A', '♥️'), ('9', '♦️')]
    assert calcular_valor(mano) == 20

def test_calcular_valor_as_como_1():
    mano = [('A', '♥️'), ('K', '♦️'), ('5', '♠️')]
    assert calcular_valor(mano) == 16 