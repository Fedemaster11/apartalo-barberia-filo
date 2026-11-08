import pytest

from apartalo.reglas import calcular_cargo_cancelacion


@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "total, horas_anticipacion, cargo_esperado",
    [
        (200, 48, 0),
        (200, 24, 0),
        (200, 23, 100),
        (200, 2, 100),
        (200, 1, 200),
    ],
)
def test_cargo_por_cancelacion(total, horas_anticipacion, cargo_esperado):
    # Dado
    # que una cita tiene un total y faltan ciertas horas para la cita

    # Cuando
    cargo = calcular_cargo_cancelacion(total, horas_anticipacion)

    # Entonces
    assert cargo == cargo_esperado


@pytest.mark.aceptacion
def test_cargo_por_no_show():
    # Dado
    total = 200
    horas_anticipacion = 48

    # Cuando
    cargo = calcular_cargo_cancelacion(
        total,
        horas_anticipacion,
        no_show=True,
    )

    # Entonces
    assert cargo == 200