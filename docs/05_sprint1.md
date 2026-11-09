# 5. Sprint 1 (27 oct – 9 nov 2026)
> Ejercicio 5 · Temas 4 y 11

## A. Planeación del sprint
> 🎩 SM facilita · 🎩 PO presenta · 🎩 desarrollador se compromete

**Objetivo del sprint:**

Implementar y probar las reglas principales de precio y cancelación de Barbería Filo, de manera que el sistema pueda calcular correctamente el total de una reserva y el cargo correspondiente cuando un cliente cancela o no se presenta.

**Capacidad en horas (Figura 2 del Tema 11):**

| Concepto | Horas |
|---|---:|
| Horas disponibles en las dos semanas | 14 |
| − Otras actividades (clases, trabajo, tareas) | 0* |
| = Disponibilidad | 14 |
| ÷ 2 = **Capacidad** | **7** |

\*Las 14 horas representan el tiempo que realmente pude apartar para el proyecto después de considerar trabajo, clases, tareas y otras actividades. Estimé aproximadamente siete días de trabajo con un promedio de dos horas diarias.

**Compromiso (historias del Sprint 1):**

| Historia | Puntos | Horas estimadas |
|---|---:|---:|
| #5 — Ver el total antes de confirmar la reserva | 5 | 2 |
| #15 — Cancelar una cita con 24 horas o más | 3 | 1 |
| #16 — Cancelar una cita entre 2 y 24 horas | 3 | 1 |
| #17 — Cancelar una cita con menos de 2 horas | 3 | 1 |
| #7 — Registrar un no-show | 3 | 1.5 |
| **Total** | **17** | **6.5** |

El compromiso utiliza 6.5 de las 7 horas de capacidad estimada, dejando un pequeño margen para ajustes e imprevistos.

Las historias seleccionadas cubren R1 mediante el cálculo del total de la reserva y R2 mediante los distintos rangos de cancelación y el caso de no-show.

**Definición de Terminado (DoD):**
1. El código correspondiente está integrado en la rama `main`.
2. Las pruebas unitarias y de aceptación relacionadas pasan correctamente con `pytest`.
3. Los criterios de aceptación de la historia fueron comprobados.
4. El código maneja correctamente las entradas inválidas cuando corresponde y no rompe pruebas que ya funcionaban.

**DoD vs. criterios de aceptación (con un ejemplo de mi backlog):**

La Definition of Done establece condiciones generales que todas las historias deben cumplir para poder considerarse terminadas. Los criterios de aceptación, en cambio, describen comportamientos específicos de cada historia.

Por ejemplo, en la historia #15 un criterio de aceptación es que una cancelación con exactamente 24 horas de anticipación no genere ningún cargo. Cumplir ese comportamiento no es suficiente para considerarla terminada: además debe tener el código integrado en `main`, sus pruebas en verde y cumplir los demás puntos de la DoD.

## B. Junta diaria — bitácora
> 🎩 desarrollador responde · 🎩 SM anota impedimentos

### 2 de noviembre de 2026
- **¿Qué hice?** Creé el repositorio desde la plantilla, completé el README con la variante Barbería Filo y trabajé en la visión y análisis del problema del Ejercicio 1.
- **¿Qué haré?** Continuar con la definición del Product Backlog y las historias de usuario.
- **¿Qué me lo impide?** Todavía necesitaba entender cómo estaban organizadas las plantillas e Issues del repositorio.

### 3 de noviembre de 2026
- **¿Qué hice?** Revisé los roles del sistema y comencé a definir las historias de usuario necesarias para cubrir las reglas R1, R2 y R3.
- **¿Qué haré?** Crear las historias como Issues utilizando la plantilla de Historia de usuario.
- **¿Qué me lo impide?** Tenía dudas sobre qué información debía ir en los criterios de aceptación y qué debía colocarse en las notas.

### 4 de noviembre de 2026
- **¿Qué hice?** Continué creando historias de usuario y revisando sus criterios de aceptación e INVEST.
- **¿Qué haré?** Terminar el backlog y agregar las historias encontradas mediante la plantilla invertida.
- **¿Qué me lo impide?** Algunas historias tenían dependencias entre sí y fue necesario revisar cuáles podían considerarse independientes.

### 5 de noviembre de 2026
- **¿Qué hice?** Terminé de organizar las historias principales del backlog y definí las dos épicas del proyecto.
- **¿Qué haré?** Agregar todos los Issues al GitHub Project y comenzar a configurar el tablero Kanban.
- **¿Qué me lo impide?** Necesitaba entender la diferencia entre los Issues del repositorio y las tarjetas que aparecen dentro del GitHub Project.

### 6 de noviembre de 2026
- **¿Qué hice?** Configuré el GitHub Project, las siete columnas del tablero Kanban y los límites WIP. También completé las políticas explícitas y las seis prácticas de Kanban.
- **¿Qué haré?** Refinar el backlog asignando prioridades y puntos a las historias.
- **¿Qué me lo impide?** Al principio no tenía claro dónde configurar los límites WIP ni cómo funcionaban los búferes de Desarrollo listo y Pruebas listo.

### 7 de noviembre de 2026
- **¿Qué hice?** Asigné prioridades MoSCoW y puntos a las historias. Calculé la carga máxima por historia y detecté que la historia de cancelación de 13 puntos debía dividirse.
- **¿Qué haré?** Crear las subhistorias de cancelación y documentar el split.
- **¿Qué me lo impide?** La historia original de cancelación era demasiado grande porque contenía los tres rangos de tiempo de R2.

### 8 de noviembre de 2026
- **¿Qué hice?** Dividí la historia de cancelación en tres historias más pequeñas, cerré la original como dividida, agregué el storyboard y escribí los escenarios BDD de R1 y R2.
- **¿Qué haré?** Comenzar la implementación y las pruebas TDD de las reglas de negocio.
- **¿Qué me lo impide?** No tengo un impedimento activo; el siguiente reto es mantener los ciclos rojo-verde correctamente registrados en los commits.

**Impedimentos y qué hizo el SM:**

| Fecha | Impedimento | Qué hizo el SM |
|---|---|---|
| 3 nov | No estaba claro qué información correspondía a criterios de aceptación y qué debía quedar como notas. | Revisó la plantilla de Historia de usuario y definió una estructura consistente para separar criterios comprobables de información contextual. |
| 6 nov | Había dudas sobre la configuración de los límites WIP y los búferes del tablero. | Revisó la consigna del ejercicio y definió WIP 2 para Aceptación, WIP 1 para Desarrollo y WIP 1 para Pruebas. |
| 7 nov | La historia de cancelación tenía 13 puntos y superaba la carga máxima de 8. | Aplicó la regla de refinamiento y dividió la historia en tres subhistorias de 3 puntos basadas en los rangos de R2. |

## C. Revisión del sprint
> 🎩 PO revisa como si fuera mi cliente

| Historia | ¿Cumple sus criterios? | ¿Aceptada? | Evidencia |
|---|---|---|---|
| #5 — Ver el total antes de confirmar la reserva | Cumple los criterios relacionados con el cálculo correcto del total, incluyendo servicio combinado y descuento de cliente frecuente. La visualización en una interfaz queda fuera del alcance del código de este sprint. | Parcialmente | Pruebas de aceptación de R1 en `tests/aceptacion/test_total_aceptacion.py` y storyboard de la pantalla. |
| #15 — Cancelar una cita con 24 horas o más | Se comprobó que con exactamente 24 horas y con más de 24 horas el cargo es $0. Queda pendiente registrar el estado de la cita como cancelada. | Parcialmente | Pruebas unitarias y pruebas de aceptación de R2. |
| #16 — Cancelar una cita entre 2 y 24 horas | Sí. Con exactamente 2 horas y con más de 2 pero menos de 24 horas se cobra el 50 % del total. Las 24 horas exactas quedan fuera de este rango. | Sí | `test_cancelacion_exactamente_2_horas_cobra_50_por_ciento` y pruebas parametrizadas de aceptación de R2. |
| #17 — Cancelar una cita con menos de 2 horas | Se comprobó que con menos de 2 horas se cobra el 100 % del total y que exactamente 2 horas no pertenece a este rango. Queda pendiente registrar el estado de la cita como cancelada. | Parcialmente | Pruebas unitarias y pruebas de aceptación de R2. |
| #7 — Registrar un no-show | Se comprobó correctamente que un no-show genera un cargo del 100 % del total. Queda pendiente almacenar o identificar el estado de la cita como no-show. | Parcialmente | `test_no_show_cobra_100_por_ciento` y prueba de aceptación de no-show. |

La suite completa de pruebas terminó con **22 pruebas aprobadas**.

**Cambio que pediría mi cliente → historia nueva:** Pendiente de crear como nueva historia del backlog.

## D. Retrospectiva
> 🎩 SM facilita

**¿Qué salió bien?**

El refinamiento previo permitió dividir la regla de cancelación en historias pequeñas y fáciles de probar. El uso de TDD ayudó a implementar las reglas de forma incremental, escribiendo primero una prueba que fallaba y después el código mínimo para hacerla pasar. Los valores límite de 2 y 24 horas quedaron cubiertos explícitamente y la suite completa terminó con 22 pruebas aprobadas.

**¿Qué hay que mejorar?**

Algunas historias mezclan reglas de negocio con comportamientos de interfaz o almacenamiento de estado. Por ejemplo, una historia puede pedir calcular correctamente un cargo y al mismo tiempo registrar la cita como cancelada. En el siguiente sprint conviene separar mejor estos comportamientos para que las historias sean más pequeñas y puedan cumplir completamente todos sus criterios de aceptación.

**Acciones para el Sprint 2:**
1. Dividir las historias que mezclen cálculo, interfaz y actualización de estado en historias independientes y más pequeñas.
2. Agregar pruebas para los estados de las citas y continuar utilizando TDD para cubrir los valores límite desde el inicio.
