# Apártalo — Barbería Filo

> Repositorio de la **Evidencia 1** de *Proyecto de ingeniería de software* (Tecmilenio, CRN 13241).

| Dato | |
|---|---|
| Estudiante | Federico David Macias Orozco |
| Matrícula | AL02990943 |
| Variante | 1 — Barbería Filo |
| Project (tablero) | Pendiente de crear |

## Visión del producto

**Apártalo Barbería Filo** es una aplicación de reservas para los clientes de la barbería de Don Rogelio. Permite reservar servicios de corte y barba, calcular automáticamente el precio y gestionar cancelaciones. Además, incluye un sistema de fidelidad para registrar las visitas y ofrecer beneficios a los clientes frecuentes. Su objetivo es reducir las citas perdidas, organizar mejor la agenda de la barbería y facilitar el proceso de reserva.

## Mi equipo Scrum (los tres sombreros)

| Sombrero | Lo que hago con él en este proyecto |
|---|---|
| 🎩 PO | Defino y priorizo las historias de usuario, interpreto las necesidades de Don Rogelio y establezco los criterios de aceptación. |
| 🎩 SM | Organizo el sprint, mantengo el tablero actualizado, identifico impedimentos y reviso que se siga el proceso Scrum. |
| 🎩 Desarrollador | Diseño la solución, programo las reglas de negocio en Python y creo las pruebas unitarias y de aceptación. |



## Cómo está organizado este repositorio

| Carpeta o archivo | Qué contiene | Ejercicio |
|---|---|---|
| `docs/01_vision_y_problema.md` | Paradigmas, manifiesto, requisito vs. solución, incertidumbre | 1 |
| Issues `historia` y `epica` + `docs/02_backlog.md` | Product backlog, plantilla invertida, glosario, iceberg | 2 |
| `docs/03_tablero.md` | Columnas, límites WIP, políticas y prácticas de kanban | 3 |
| `docs/04_refinamiento.md` + `features/` | Grooming, carga máxima, división, escenarios BDD, tabla FIT | 4 |
| `docs/05_sprint1.md` | Planeación, bitácora, revisión y retrospectiva | 5 |
| `src/apartalo/` + `tests/` + `docs/06_tdd.md` | Código, pruebas y ciclos de TDD | 6 |
| Issues `rnf` + `docs/07_rnf.md` | Requisitos no funcionales | 7 |
| `metricas/` + `docs/08_metricas.md` | Fotografía del tablero y consultas SQL | 8 |
| `ENTREGA.md` | Enlaces a cada evidencia | Entrega |

## Cómo correr las pruebas

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                           # todas las pruebas
pytest -m aceptacion             # solo la suite de aceptación
pytest -m unitaria               # solo las unitarias
pytest -m rnf                    # solo las de requisitos no funcionales
```
