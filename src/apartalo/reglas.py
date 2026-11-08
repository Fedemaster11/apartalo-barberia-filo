"""Reglas de negocio de mi variante (Ejercicio 6).

Aquí van las funciones de R1 y R2. Escríbelas con TDD:
primero una prueba que falle (ROJO), luego el código mínimo para que pase (VERDE),
y después mejora el código sin romper las pruebas (REFACTOR).

Si una entrada no tiene sentido (horas negativas, un servicio que no existe, etc.),
la función debe lanzar ValueError.
"""
def calcular_total(corte, barba, visitas_mes):
    if corte and barba:
        total = 255
    elif corte and not barba:
        total = 180
    else:
        return None

    if visitas_mes >= 5:
        total -= 20

    return total

def calcular_cargo_cancelacion(total, horas_anticipacion):
    if horas_anticipacion < 2:
        return total

    if 2 <= horas_anticipacion < 24:
        return total * 0.5

    if horas_anticipacion >= 24:
        return 0