# language: es
Característica: Cargo por cancelación en Barbería Filo

  Esquema del escenario: Calcular el cargo según las horas de anticipación
    Dado que una cita tiene un total de <total> pesos y faltan <horas> horas para la cita
    Cuando el cliente cancela la cita
    Entonces el cargo por cancelación es de <cargo> pesos

    Ejemplos:
      | total | horas | cargo |
      | 200   | 48    | 0     |
      | 200   | 24    | 0     |
      | 200   | 23    | 100   |
      | 200   | 2     | 100   |
      | 200   | 1     | 200   |

  Escenario: Cliente no se presenta a la cita
    Dado que una cita tiene un total de 200 pesos
    Cuando el cliente no se presenta
    Entonces el cargo es de 200 pesos
