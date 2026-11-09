# 7. Requisitos no funcionales
> Ejercicio 7 · Tema 9 · 🎩 PO y 🎩 desarrollador
> Cada restricción va como **issue** (formulario "Requisito no funcional"). Aquí va el resumen.

| Issue | Restricción SMART | Externa / interna | Cualidad | Historia (T) | Prueba práctica (Tabla 2) o práctica (Tabla 4) |
|---|---|---|---|---|---|
| #19 | Durante la hora pico de los sábados de 10:00 a 14:00, el sistema deberá procesar al menos 40 solicitudes de reserva por hora sin rechazar más del 1 % por causa de la carga. | Externa | Escalabilidad | #1 | Prueba de carga (load testing): simular al menos 40 solicitudes por hora y verificar que al menos el 99 % sean procesadas correctamente. |
| #20 | El 100 % de las entradas inválidas definidas para las reglas de precio y cancelación, como horas negativas o una reserva sin servicio seleccionado, deberán rechazarse mediante `ValueError` sin producir resultados incorrectos. | Externa | Robustez | #16 | Probar entradas inválidas y comprobar que el sistema lance `ValueError` en el 100 % de los casos definidos. |
| #21 | Los cambios realizados para la historia #18 deberán integrarse a la rama `main` en un máximo de 24 horas después de completarse y, después de cada integración, el 100 % de las pruebas existentes deberá continuar en verde. | Interna | Mantenimiento | #18 | Integración continua: integrar cambios al menos una vez al día y ejecutar la suite de pruebas después de cada integración. |

## 7.3 La que compruebo con código

- **Restricción:** #20 — RNF: Rechazar entradas inválidas sin fallar.
- **Prueba:** `tests/rnf/test_robustez.py`

La prueba verifica dos entradas inválidas: horas de anticipación negativas y una reserva sin ningún servicio seleccionado. En ambos casos se comprueba que el sistema lance `ValueError`.

La suite específica de requisitos no funcionales terminó con **2 pruebas aprobadas**, y la suite completa terminó con **24 pruebas aprobadas**.

## 7.4 Una por sprint

- **La que agrego a mi DoD en el Sprint 1:** #20 — Robustez. La agrego porque las reglas R1 y R2 fueron implementadas en este sprint y ya existen pruebas automatizadas que comprueban que las entradas inválidas sean rechazadas correctamente.

- **Las que dejo para después y por qué:** #19 — Escalabilidad se deja para un sprint posterior porque todavía no existe el flujo completo de reservas necesario para realizar una prueba de carga realista de 40 reservas por hora. #21 — Mantenimiento se aplicará en un sprint posterior, especialmente cuando se implemente la historia #18, porque esa restricción está trazada directamente a esa historia y requiere observar el proceso de integración de sus cambios.
