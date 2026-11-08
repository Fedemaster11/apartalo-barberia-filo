import pytest

from apartalo.reglas import calcular_total


@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "corte, barba, visitas_mes, total_esperado",
    [
        (True, False, 0, 180),
        (False, True, 0, 120),
        (True, True, 0, 255),
        (True, True, 4, 255),
        (True, True, 5, 235),
    ],
)
def test_total_del_servicio(corte, barba, visitas_mes, total_esperado):
    # Dado
    # que un cliente selecciona servicios y tiene cierto número de visitas

    # Cuando
    total = calcular_total(corte, barba, visitas_mes)

    # Entonces
    assert total == total_esperado