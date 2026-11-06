# 3. El tablero kanban

> Ejercicio 3 · Tema 3 · 🎩 SM

## 3.2 Límites WIP

| **Columna** | **Límite** | **Por qué ese número** |
| ----------- | ---------- | ---------------------- |
| Aceptación  | 2 | Como soy una sola persona, puedo revisar y refinar como máximo dos historias a la vez sin acumular demasiado trabajo pendiente. |
| Desarrollo  | 1 | Solo desarrollo una historia a la vez para evitar multitarea y terminar el trabajo antes de comenzar otra historia. |
| Pruebas     | 1 | Pruebo una historia a la vez para detectar y corregir problemas antes de comenzar a probar otra. |

## 3.3 Políticas explícitas

| **Para pasar a…** | **La tarjeta debe cumplir…** |
| ----------------- | ---------------------------- |
| Aceptación | Tener definido el rol, el deseo y el beneficio, además de contar con al menos dos criterios de aceptación. |
| Desarrollo | Tener criterios de aceptación claros, revisión INVEST realizada y estar suficientemente pequeña y entendida para comenzar a desarrollarse. |
| Desarrollo listo | La funcionalidad correspondiente ya fue implementada, el código está en el repositorio y no quedan tareas de desarrollo pendientes. |
| Pruebas | La funcionalidad terminó su desarrollo y existe capacidad disponible en la columna Pruebas. |
| Pruebas listo | Las pruebas correspondientes pasan correctamente y se comprobaron los criterios de aceptación de la historia. |
| Liberación | La historia cumple con su Definition of Done, sus pruebas pasan y está lista para considerarse terminada. |

## 3.4 Las seis prácticas de kanban en mi tablero

| **Práctica**                                    | **Cómo la aplico (o por qué todavía no aplica)** |
| ----------------------------------------------- | ------------------------------------------------ |
| 1. Visualizar el trabajo | Cada historia se representa mediante una tarjeta y se mueve por las siete columnas del tablero según su estado real. |
| 2. Limitar el WIP | Uso límites de 2 historias en Aceptación, 1 en Desarrollo y 1 en Pruebas para evitar acumular trabajo y reducir la multitarea. |
| 3. Administrar el flujo | Muevo las historias únicamente cuando cumplen las condiciones de la siguiente etapa y observo dónde se acumula trabajo. |
| 4. Hacer explícitas las políticas | Definí condiciones claras que una tarjeta debe cumplir antes de pasar a cada columna del tablero. |
| 5. Implementar ciclos de retroalimentación | La revisión de criterios de aceptación y las pruebas permiten detectar problemas y realizar ajustes antes de liberar una historia. |
| 6. Mejora colaborativa y evolución experimental | El proyecto es individual, por lo que no existe colaboración entre varios integrantes; sin embargo, revisaré el flujo, los resultados y las métricas del sprint para ajustar y mejorar mi proceso en los siguientes sprints. |
