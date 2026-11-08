import pytest

from apartalo.reglas import calcular_total


@pytest.mark.unitaria
def test_corte_cuesta_180():
    # Dado
    corte = True
    barba = False
    visitas_mes = 0

    # Cuando
    total = calcular_total(corte, barba, visitas_mes)

    # Entonces
    assert total == 180