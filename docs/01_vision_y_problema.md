# 1. Visión y problema correcto
> Ejercicio 1 · Temas 1, 2 y 5 · 🎩 PO
> La visión va en el `README.md`. Aquí van los puntos 2 a 6.

## 1.2 ¿Por qué no cascada?

| Causa de falla de cascada | Cómo se vería en mi proyecto |
|---|---|
| Requisitos incompletos o cambiantes | Don Rogelio todavía no tiene claro si quiere cobrar por adelantado y algunas necesidades, como el programa para clientes frecuentes, todavía necesitan definirse con mayor detalle. Si se fijara todo desde el inicio, sería probable tener que modificarlo después. |
| Retroalimentación demasiado tardía | Si construyera toda la aplicación antes de enseñársela a Don Rogelio, podría descubrir al final que el flujo de reserva o las funciones propuestas no resuelven realmente su problema de citas perdidas. |

Sí usaría prototipos. Los utilizaría antes de desarrollar por completo funciones como el flujo de reserva y el programa de fidelidad, para enseñárselos a Don Rogelio, obtener retroalimentación y ajustar los requisitos antes de invertir más tiempo en el desarrollo.

## 1.3 El manifiesto en mi proyecto

| Valor o principio | Decisión concreta en mi proyecto |
|---|---|
| Valor: Software funcionando sobre documentación extensiva | Al final del Sprint 1 entregaré las reglas R1 y R2 funcionando y comprobadas con pruebas, en lugar de dedicar el sprint a producir únicamente documentación. |
| Valor: Colaboración con el cliente sobre negociación contractual | Las dudas y cambios de Don Rogelio se convertirán en historias del backlog y se validarán mediante criterios de aceptación y revisiones del sprint. |
| Principio: Entregar software funcionando frecuentemente | Dividiré el trabajo en sprints y entregaré primero funciones pequeñas y comprobables, como el cálculo del total y la cancelación. |
| Principio: Aceptar cambios en los requisitos | Si Don Rogelio cambia su decisión sobre anticipos o beneficios para clientes frecuentes, actualizaré y volveré a priorizar el backlog en lugar de mantener un plan fijo. |

## 1.4 Frameworks

| Framework | Lo que tomo de él |
|---|---|
| Scrum | Sprints, Product Backlog, Sprint Planning, Sprint Review, retrospectiva y los tres sombreros de PO, SM y desarrollador. |
| Kanban | El tablero visual, el movimiento de las historias entre estados y los límites WIP para no trabajar en demasiadas cosas al mismo tiempo. |
| XP | TDD, pruebas frecuentes, código sencillo y ciclos rojo → verde → refactor para implementar las reglas de negocio. |

La combinación de Scrum y Kanban se llama: **Scrumban**.

## 1.5 Requisito o solución

| # | Lo que dijo mi cliente | ¿Requisito o solución? | Si es solución: el requisito que hay detrás |
|---|---|---|---|
| 1 | “Me dejan plantado mucho los sábados y pierdo dinero.” | Requisito / problema | — |
| 2 | “Quiero un botón verde grande que diga RESERVAR, como el de WhatsApp.” | Solución | El cliente necesita una forma clara, sencilla y visible de iniciar una reserva. |
| 3 | “Los clientes de siempre se merecen algo.” | Requisito | — |
| 4 | “Que me llegue la agenda del día en un Excel.” | Solución | Don Rogelio necesita consultar y conservar de forma sencilla la agenda diaria de citas. |
| 5 | “No sé si cobrar por adelantado; me da miedo que la gente ya no reserve.” | Requisito todavía incierto | — |

## 1.6 Incertidumbre

- **Incertidumbre del qué:** alta, porque Don Rogelio conoce el problema principal, pero todavía existen decisiones de negocio sin resolver, especialmente si debe cobrar anticipos y cómo funcionarán algunos beneficios para clientes frecuentes.
- **Incertidumbre del cómo:** baja, porque para esta evidencia la solución técnica está acotada: usaré Python, pytest, GitHub y reglas de negocio sencillas, sin interfaz gráfica ni base de datos.
- **Zona del diagrama:** **Compleja**, porque existe incertidumbre importante sobre lo que realmente necesita el cliente, aunque la implementación técnica inicial sea relativamente conocida.
- **Qué haré en este sprint para bajar la incertidumbre del qué:** conversar y validar las historias con Don Rogelio, crear ejemplos y criterios de aceptación, utilizar un prototipo sencillo del flujo de reserva y probar primero R1 y R2 antes de agregar funciones menos definidas.
