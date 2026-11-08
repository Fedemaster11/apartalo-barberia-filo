# 6. Pruebas de aceptación y TDD
> Ejercicio 6 · Tema 8 · 🎩 desarrollador

## 6.2 Mis ciclos de TDD

| Ciclo | Commit ROJO | Commit VERDE | Commit REFACTOR (si hubo) | Qué aprendí |
|---|---|---|---|---|
| 1 | [57fd363 - ROJO: prueba de precio para un corte](https://github.com/Fedemaster11/apartalo-barberia-filo/commit/57fd3637d05c5d3f01a142c328dec93d41663ee1) | [196c390 - VERDE: calcular precio de corte en 180](https://github.com/Fedemaster11/apartalo-barberia-filo/commit/196c390b83cadeb1cb5fa5e22bb3aa166127c98b) | No fue necesario | Primero escribí una prueba que fallaba porque `calcular_total` todavía no existía. Después implementé únicamente el código necesario para que un corte costara $180 y la prueba pasara. |
| 2 | [f1f085d - ROJO: prueba de descuento en corte y barba](https://github.com/Fedemaster11/apartalo-barberia-filo/commit/f1f085d50346ad120768cde37225f917a54200c6) | [8c73b90 - VERDE: aplicar descuento a corte y barba](https://github.com/Fedemaster11/apartalo-barberia-filo/commit/8c73b90aa6a6cb1e04589cd3dc965ab9b9bdf708) | No fue necesario | La nueva prueba obligó a extender la función para distinguir el servicio individual del servicio combinado. Se implementó el 15 % de descuento para corte y barba juntos, dando un total de $255. |
| 3 | [84ef83c - ROJO: prueba de descuento para cliente frecuente](https://github.com/Fedemaster11/apartalo-barberia-filo/commit/84ef83c0b8ce37f0ca159769a207583c5b811c71) | [6e52248 - VERDE: aplicar descuento a cliente frecuente](https://github.com/Fedemaster11/apartalo-barberia-filo/commit/6e522480faa314e3d6954310e37e6ec125262ba6) | No fue necesario | La prueba del límite de 5 visitas permitió comprobar que el descuento de cliente frecuente debía aplicarse después del descuento del servicio combinado, reduciendo el total de $255 a $235. |

Además de los tres ciclos mínimos documentados, continué aplicando TDD para otros casos de R1 y R2, entre ellos:

- Precio del servicio de barba.
- Reserva sin ningún servicio seleccionado.
- Cancelación con menos de 2 horas.
- Cancelación con exactamente 2 horas.
- Cancelación con exactamente 24 horas.
- Horas de anticipación negativas.
- No-show.

Las pruebas unitarias se encuentran en `tests/unitarias/`.

Las pruebas de aceptación derivadas de los escenarios BDD se encuentran en `tests/aceptacion/` y utilizan `@pytest.mark.parametrize` para ejecutar las filas de las tablas de Ejemplos.

Al finalizar las pruebas unitarias y de aceptación, la suite completa terminó con **22 pruebas aprobadas**.

## 6.6 Cobertura de caminos

- **Función:** `calcular_cargo_cancelacion`
- **Caminos** (cada `return` y cada `raise`): 5
  1. Si `horas_anticipacion < 0`, la función lanza `ValueError`.
  2. Si `no_show=True`, la función devuelve el 100 % del total.
  3. Si la cancelación ocurre con menos de 2 horas de anticipación, devuelve el 100 % del total.
  4. Si ocurre con 2 horas o más, pero menos de 24 horas, devuelve el 50 % del total.
  5. Si ocurre con 24 horas o más de anticipación, devuelve 0.
- **Caminos que recorren mis pruebas:** 5 de 5.
- **Cobertura:** 100 % de los caminos identificados para `calcular_cargo_cancelacion`.
- **Pruebas que agregué para completar:** horas negativas, no-show, menos de 2 horas, exactamente 2 horas y exactamente 24 horas.

## 6.7 Regresión

- **Defecto** (encontrado o provocado): Se provocó deliberadamente un defecto cambiando temporalmente la condición de cancelación de `horas_anticipacion >= 24` a `horas_anticipacion > 24`.
- **Prueba que lo detecta:** `test_cancelacion_exactamente_24_horas_no_cobra`.
- **Qué pasaba y cómo lo corregí:** Al cambiar `>= 24` por `> 24`, una cancelación realizada exactamente 24 horas antes ya no entraba en ningún caso y la función devolvía `None` en lugar de `0`. La prueba del valor límite falló y detectó la regresión. Después restauré la condición correcta `>= 24` y la suite completa volvió a terminar con **22 pruebas aprobadas**.
