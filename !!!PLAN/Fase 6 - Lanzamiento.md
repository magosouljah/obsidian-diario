# Fase 6 — Ensayo, soft launch y publicación

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 5–9 de octubre  
**Objetivo:** promover el RC sin cambiarlo, observar y abrir gradualmente.

## Día 31 — 5 de octubre — Ensayo final de producción

**Resultado:** cada operación irreversible se ejecuta una vez de forma controlada.

### Tarea 31.1 [P0 · QA/LF/OP] — Transacción real controlada

- [ ] Owner crea cuenta limpia, verifica, compra, recibe entitlement, cancela y obtiene refund.
- [ ] Reconciliar Stripe/BeatGaler/banco según disponibilidad y borrar/exportar cuenta de prueba.
- [ ] Confirmar emails, Terms version, support ticket y status link.

### Tarea 31.2 [P0 · QA/DE/OP] — Disaster rehearsal

- [ ] Instalar descargas públicas candidatas en equipos limpios.
- [ ] Backup→restore, app rollback, updater rollback y cierre de registro/pagos/uploads.
- [ ] Verificar que todas las alertas llegan al owner de guardia.

**Dependencias:** RC.  
**Evidencia:** conciliación a cero, install logs y runbook timestamps.  
**Gate de salida:** ensayo completo sin intervención improvisada.

## Día 32 — 6 de octubre — Soft launch a 25 usuarios

**Resultado:** producción atiende una cohorte limitada con soporte activo.

### Tarea 32.1 [P0/P1 · RO/OP] — Apertura gradual

- [ ] 25 invitaciones propuestas, límite de registros y capacidad reservada.
- [ ] Web y descargas desde URLs definitivas; stable updater solo para cohorte.
- [ ] Staff de incidente, soporte y pagos disponible.

### Tarea 32.2 [P1 · QA/OP] — Observación

- [ ] Revisar a 15 min, 1 h, 4 h y 8 h: auth, errors, latency, DB, Stripe, bots, queues.
- [ ] Contactar usuarios afectados y pausar con kill switch si cruza threshold.
- [ ] Hotfix solo P0/P1 mediante nueva RC y smoke.

**Dependencias:** Día 31.  
**Evidencia:** dashboard anotado y ledger de cohortes/incidentes.  
**Gate de salida:** 8 horas sin P0/P1 y 100% de pagos reconciliados.

## Día 33 — 7 de octubre — Soak de 24 horas

**Resultado:** operación estable durante un ciclo completo.

### Tarea 33.1 [P1 · OP/LF] — Continuidad

- [ ] Monitorear jobs nocturnos, backups, session expiry, webhooks y bot maintenance.
- [ ] Responder tickets bajo SLA propuesto y probar handoff de guardia.
- [ ] Revisar logs por secretos/datos y alertas ruidosas/silenciosas.

### Tarea 33.2 [P1 · RO/QA] — Cohort review

- [ ] Core-flow completion, crashes, errores, conversion y soporte por plataforma.
- [ ] Reconciliar pagos/planes y storage/index.
- [ ] Decidir continuar, mantener cohorte o rollback.

**Dependencias:** soft launch activo.  
**Evidencia:** informe 24 h y reconciliación.  
**Gate de salida:** 24 h sin incidente crítico y sin deuda de datos/dinero.

## Día 34 — 8 de octubre — Decisión pública

**Resultado:** una decisión binaria, auditable y comunicable.

### Tarea 34.1 [P0 · RO + approvers] — Go/no-go

- [ ] Revisar cada gate obligatorio y owner confirmation.
- [ ] Security, QA, Desktop, Ops, Legal/Finance y Support firman o bloquean.
- [ ] Cualquier P0/P1, pago no reconciliado o plataforma no probada produce NO-GO.

### Tarea 34.2 [P1 · RO/LF] — Preparar comunicación

- [ ] Landing, downloads, checksum/signature help, pricing, FAQ, status y support.
- [ ] Anuncio y rollback/delay message preparados antes de abrir.
- [ ] Snapshot final de datos/config y staffing de 8 horas.

**Dependencias:** soak aprobado.  
**Evidencia:** acta go/no-go y checklist firmada.  
**Gate de salida:** solo un GO unánime de gates permite el Día 35.

## Día 35 — 9 de octubre — Lanzamiento público

**Resultado:** BeatGaler disponible públicamente con rollout controlado.

### Tarea 35.1 [P0 · OP/RO] — Rollout

- [ ] Abrir 10%, luego 50% y 100% de capacidad propuesta solo tras checkpoints.
- [ ] Abrir registro, Web, Windows, macOS y planes desde el mismo release dossier.
- [ ] Congelar cambios no críticos; rollback/kill switches listos.

### Tarea 35.2 [P1 · Todos] — Operar ocho horas

- [ ] Seguimiento continuo de seguridad, errores, pagos, datos, bots, tickets y downloads.
- [ ] Reconciliar cada compra y muestrear export/delete/updater.
- [ ] Publicar status transparente; incident command ante cualquier threshold.

**Dependencias:** GO del Día 34.  
**Evidencia:** snapshots pre/post, dashboard, ledger de release y reporte de 8 h.  
**Gate de salida:** 100% abierto o rollback controlado; nunca estado ambiguo.
