import pytest

from apartalo.reglas import calcular_total, calcular_cargo_cancelacion


@pytest.mark.rnf
def test_rnf_horas_negativas_lanza_value_error():
    # Una cancelación con horas negativas es una entrada inválida
    with pytest.raises(ValueError):
        calcular_cargo_cancelacion(200, -1)


@pytest.mark.rnf
def test_rnf_reserva_sin_servicio_lanza_value_error():
    # Una reserva sin corte ni barba es una entrada inválida
    with pytest.raises(ValueError):
        calcular_total(False, False, 0)