# language: es
Característica: Total del servicio en Barbería Filo

  Esquema del escenario: Calcular el total según servicios y visitas del mes
    Dado que un cliente selecciona corte "<corte>" y barba "<barba>" y tiene <visitas> visitas en el mes
    Cuando se calcula el total del servicio
    Entonces el total es de <total> pesos

    Ejemplos:
      | corte | barba | visitas | total |
      | sí    | no    | 0       | 180   |
      | no    | sí    | 0       | 120   |
      | sí    | sí    | 0       | 255   |
      | sí    | sí    | 4       | 255   |
      | sí    | sí    | 5       | 235   |
