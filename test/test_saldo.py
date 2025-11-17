import pytest

@pytest.fixture
def saldo_inicial():
    return 100000

@pytest.fixture
def apuesta():
    return 50000

def test_saldo_inicial(saldo_inicial):
    assert saldo_inicial == 100000

@pytest.mark.parametrize("num_perdidas,saldo_esperado", [
    (1, 50000),
    (2, 0),
])

def test_saldo_despues_perdidas(saldo_inicial, apuesta, num_perdidas, saldo_esperado):
    saldo = saldo_inicial
    for _ in range(num_perdidas):
        saldo -= apuesta
    assert saldo == saldo_esperado

def test_no_puede_jugar_sin_dinero(apuesta):
    saldo = 0
    puede_jugar = saldo >= apuesta
    assert puede_jugar == False



@pytest.mark.parametrize("saldo,puede_jugar_esperado", [
    (100000, True),
    (50000, True),
    (49999, False),
    (0, False),
])
def test_verificar_saldo_suficiente(saldo, apuesta, puede_jugar_esperado):
    puede_jugar = saldo >= apuesta
    assert puede_jugar == puede_jugar_esperado


@pytest.mark.parametrize("victorias,derrotas,saldo_esperado", [
    (2, 1, 150000),  
    (1, 1, 100000), 
    (3, 2, 150000), 
])
def test_saldo_con_victorias_y_derrotas(saldo_inicial, apuesta, victorias, derrotas, saldo_esperado):
    saldo = saldo_inicial
    saldo += (victorias * apuesta)
    saldo -= (derrotas * apuesta)
    assert saldo == saldo_esperado