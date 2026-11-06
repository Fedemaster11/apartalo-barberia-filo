# 2. El product backlog
> Ejercicio 2 · Tema 6 · 🎩 PO
> Las historias van como **issues** (formulario "Historia de usuario"). Aquí va lo demás.

## 2.1 Roles

| Rol | Quién es | Qué desea |
|---|---|---|
| Cliente | Persona que reserva servicios en Barbería Filo | Reservar fácilmente, conocer el precio, cancelar una cita y recibir beneficios por fidelidad. |
| Don Rogelio | Dueño y administrador de Barbería Filo | Organizar la agenda, reducir las citas perdidas y controlar las reglas del negocio. |
| Sistema de recordatorios | Servicio automático de la aplicación | Avisar al cliente sobre su próxima cita para reducir olvidos y ausencias. |

## 2.4 Plantilla invertida: historias que me faltaban

`Para poder <beneficio>, como <rol>, quiero <deseo>`

| Beneficio que revisé | Historia que encontré | Issue |
|---|---|---|
| Para poder elegir cuándo ir a la barbería | Como cliente, quiero consultar los horarios disponibles, para elegir una hora antes de reservar. | Pendiente |
| Para poder aplicar correctamente los beneficios de cliente frecuente | Como Don Rogelio, quiero registrar cuándo una cita fue completada, para llevar correctamente el número de visitas del cliente. | Pendiente |

¿Cómo me ayudó ordenar por beneficio?

Ordenar primero por el beneficio me ayudó a pensar en lo que el usuario realmente necesita lograr y no solamente en funciones aisladas. De esta forma encontré historias que había dado por supuestas, como consultar los horarios disponibles antes de reservar y registrar una visita completada para poder calcular correctamente los beneficios de fidelidad.

## 2.5 Glosario (lenguaje ubicuo)

| Término | Qué significa para mi cliente |
|---|---|
| Cita | Reserva de un cliente para recibir uno o más servicios en una fecha y hora determinadas. |
| Cliente frecuente | Cliente que ha realizado 5 visitas o más durante el mismo mes y recibe $20 de descuento. |
| Servicio combinado | Reserva de corte y barba juntos, a la que se aplica 15 % de descuento sobre la suma de ambos servicios. |
| Cancelación tardía | Cancelación realizada con menos de 24 horas de anticipación y que puede generar un cargo según el tiempo restante. |
| No-show | Cliente que tenía una cita reservada pero no se presentó; se le cobra 100 % del total. |

## 2.6 El iceberg

- **En la punta:** las historias más claras, pequeñas y prioritarias para el primer sprint, como calcular el total de los servicios, aplicar los descuentos de R1 y calcular los cargos de cancelación de R2.
- **En el fondo:** historias menos urgentes o todavía grandes y poco definidas, como el programa completo de fidelidad, el décimo corte gratis y la administración avanzada de la agenda.
- **Por qué:** las historias de la punta están mejor entendidas, son necesarias para las reglas principales del negocio y pueden desarrollarse y probarse pronto. Las del fondo todavía necesitan más conversación, refinamiento o división antes de entrar a un sprint.
