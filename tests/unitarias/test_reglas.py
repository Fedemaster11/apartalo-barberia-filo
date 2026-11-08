import pytest

from apartalo.reglas import calcular_total, calcular_cargo_cancelacion


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
    
@pytest.mark.unitaria
def test_cancelacion_menos_de_2_horas_cobra_100_por_ciento():
    # Dado
    total = 200
    horas_anticipacion = 1

    # Cuando
    cargo = calcular_cargo_cancelacion(total, horas_anticipacion)

    # Entonces
    assert cargo == 200
    
@pytest.mark.unitaria
def test_cancelacion_exactamente_2_horas_cobra_50_por_ciento():
    # Dado
    total = 200
    horas_anticipacion = 2

    # Cuando
    cargo = calcular_cargo_cancelacion(total, horas_anticipacion)

    # Entonces
    assert cargo == 100
    
@pytest.mark.unitaria
def test_cancelacion_exactamente_24_horas_no_cobra():
    # Dado
    total = 200
    horas_anticipacion = 24

    # Cuando
    cargo = calcular_cargo_cancelacion(total, horas_anticipacion)

    # Entonces
    assert cargo == 0
    
@pytest.mark.unitaria
def test_cancelacion_con_horas_negativas_lanza_error():
    # Dado
    total = 200
    horas_anticipacion = -1

    # Cuando / Entonces
    with pytest.raises(ValueError):
        calcular_cargo_cancelacion(total, horas_anticipacion)
        
@pytest.mark.unitaria
def test_barba_cuesta_120():
    # Dado
    corte = False
    barba = True
    visitas_mes = 0

    # Cuando
    total = calcular_total(corte, barba, visitas_mes)

    # Entonces
    assert total == 120
    
@pytest.mark.unitaria
def test_sin_servicio_lanza_error():
    # Dado
    corte = False
    barba = False
    visitas_mes = 0

    # Cuando / Entonces
    with pytest.raises(ValueError):
        calcular_total(corte, barba, visitas_mes)
    
@pytest.mark.unitaria
def test_no_show_cobra_100_por_ciento():
    # Dado
    total = 200
    horas_anticipacion = 48

    # Cuando
    cargo = calcular_cargo_cancelacion(
        total,
        horas_anticipacion,
        no_show=True
    )

    # Entonces
    assert cargo == 200