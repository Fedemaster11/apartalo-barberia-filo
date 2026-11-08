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
    
    

@pytest.mark.unitaria
def test_corte_y_barba_tienen_15_por_ciento_descuento():
    # Dado
    corte = True
    barba = True
    visitas_mes = 0

    # Cuando
    total = calcular_total(corte, barba, visitas_mes)

    # Entonces
    assert total == 255
    
    
@pytest.mark.unitaria
def test_cliente_frecuente_recibe_20_pesos_de_descuento():
    # Dado
    corte = True
    barba = True
    visitas_mes = 5

    # Cuando
    total = calcular_total(corte, barba, visitas_mes)

    # Entonces
    assert total == 235