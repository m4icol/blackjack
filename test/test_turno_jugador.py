import pytest
from turnos import jugador_gana, es_empate
from barajas import calcular_valor

@pytest.fixture
def mano_jugador_19():
    return [('K', '♥️'), ('9', '♦️')]

@pytest.fixture
def mano_dealer_17():
    return [('K', '♠️'), ('7', '♣️')]

def test_jugador_gana_con_mayor_valor(mano_jugador_19, mano_dealer_17):
    assert jugador_gana(mano_jugador_19, mano_dealer_17) == True



@pytest.mark.parametrize("mano_jugador,mano_dealer,esperado", [
    ([('K', '♥️'), ('9', '♦️')], [('K', '♠️'), ('7', '♣️')], True), 
    ([('K', '♥️'), ('8', '♦️')], [('K', '♠️'), ('9', '♣️')], False),
    ([('K', '♥️'), ('10', '♦️')], [('9', '♠️'), ('9', '♣️')], True),
])
def test_jugador_gana_diferentes_escenarios(mano_jugador, mano_dealer, esperado):
    assert jugador_gana(mano_jugador, mano_dealer) == esperado

def test_jugador_pierde_con_menor_valor():
    mano_jugador = [('K', '♥️'), ('7', '♦️')] 
    mano_dealer = [('K', '♠️'), ('9', '♣️')]
    assert jugador_gana(mano_jugador, mano_dealer) == False

def test_jugador_pierde_si_se_pasa():
    mano_jugador = [('K', '♥️'), ('K', '♦️'), ('5', '♠️')] 
    mano_dealer = [('K', '♠️'), ('7', '♣️')]  
    assert jugador_gana(mano_jugador, mano_dealer) == False

def test_jugador_gana_si_dealer_se_pasa():
    mano_jugador = [('K', '♥️'), ('9', '♦️')] 
    mano_dealer = [('K', '♠️'), ('K', '♣️'), ('5', '♥️')] 
    assert jugador_gana(mano_jugador, mano_dealer) == True



@pytest.mark.parametrize("valor", [19, 20, 21, 18])
def test_es_empate_con_mismo_valor(valor):
    if valor == 21:
        mano_jugador = [('K', '♥️'), ('A', '♦️')]
        mano_dealer = [('Q', '♠️'), ('A', '♣️')]
    elif valor == 20:
        mano_jugador = [('K', '♥️'), ('Q', '♦️')]
        mano_dealer = [('J', '♠️'), ('K', '♣️')]
    elif valor == 19:
        mano_jugador = [('K', '♥️'), ('9', '♦️')]
        mano_dealer = [('Q', '♠️'), ('9', '♣️')]
    else:
        mano_jugador = [('K', '♥️'), ('8', '♦️')]
        mano_dealer = [('Q', '♠️'), ('8', '♣️')]
    
    assert es_empate(mano_jugador, mano_dealer) == True