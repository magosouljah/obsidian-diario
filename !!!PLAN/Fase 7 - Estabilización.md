# Fase 7 — Buffer y estabilización

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 10–16 de octubre  
**Objetivo:** proteger datos/dinero, estabilizar y convertir feedback en roadmap.

## Día 36 — 10–11 de octubre — Guardia de fin de semana

**Resultado:** cobertura continua sin introducir cambios de alcance.

### Tarea 36.1 [P0/P1 · OP/Support] — Triage

- [ ] Vigilar cuentas, pagos, corrupción, cross-tenant, updater y firma.
- [ ] Hotfix solo con repro, test, approval, canary y rollback.
- [ ] Mantener status y comunicación a usuarios afectados.

**Dependencias:** lanzamiento.  
**Evidencia:** handoff y timeline de incidentes.  
**Gate de salida:** ningún P0/P1 sin owner/respuesta.

## Día 37 — 12 de octubre — Conciliación y restore de rutina

**Resultado:** dinero y datos cierran sin excepciones ocultas.

### Tarea 37.1 [P0 · LF/BE/OP] — Cierre operativo

- [ ] Stripe↔BeatGaler, refunds/disputes, entitlements y cuentas huérfanas.
- [ ] Verificar backup diario y restaurar una muestra aislada.
- [ ] Revisar garbage journal, Trash physical deletes y bot memberships.

**Dependencias:** datos del lanzamiento.  
**Evidencia:** conciliación a cero o cola con owner/SLA.  
**Gate de salida:** sin deuda financiera o de integridad no explicada.

## Día 38 — 13 de octubre — Rendimiento y capacidad real

**Resultado:** configuración se ajusta a tráfico observado, no a intuición.

### Tarea 38.1 [P2 · OP/FE/BE] — Analizar

- [ ] p50/p95/p99, Web vitals, memory, chunk/cache, uploads, lease y queue por plataforma.
- [ ] Comparar pico real con envelope y margen; ajustar admission/alerts.
- [ ] Priorizar thumbnails/lazy load/query/indexes donde la evidencia lo muestre.

**Dependencias:** telemetría suficiente.  
**Evidencia:** reporte antes/después y budgets.  
**Gate de salida:** capacity plan actualizado sin ampliar innecesariamente la flota.

## Día 39 — 14 de octubre — Experiencia y soporte

**Resultado:** feedback se convierte en problemas reproducibles y prioridades.

### Tarea 39.1 [P2/P3 · DL/QA/Support] — Síntesis

- [ ] Agrupar fricción por flujo/plataforma; separar bug, copy, educación y feature.
- [ ] Revisar abandono de onboarding/import/checkout y top tickets.
- [ ] Mantener P0/P1 en carril inmediato; P2/P3 al roadmap.

**Dependencias:** métricas/tickets.  
**Evidencia:** insight→evidencia→owner→fecha.  
**Gate de salida:** backlog priorizado sin duplicados ni peticiones vagas.

## Día 40 — 15 de octubre — Patch candidate

**Resultado:** primera actualización pequeña y segura, solo si hace falta.

### Tarea 40.1 [P1/P2 · Owners/QA] — Preparar `1.0.1`

- [ ] Elegir fixes de alto impacto/bajo riesgo; no rediseño amplio.
- [ ] Suite completa afectada, firmas, notarización y beta ring.
- [ ] Update/rollback y release notes verificadas.

**Dependencias:** backlog y necesidad real.  
**Evidencia:** release dossier de patch.  
**Gate de salida:** publicar solo si mejora riesgo neto; si no, no forzar versión.

## Día 41 — 16 de octubre — Postmortem y roadmap

**Resultado:** lanzamiento cerrado como aprendizaje operacional.

### Tarea 41.1 [P2 · RO/Todos] — Revisión

- [ ] Qué funcionó, qué falló, detección, respuesta y costos.
- [ ] Actualizar runbooks, gates, SLOs y ownership.
- [ ] Priorizar i18n, motion de deleite, stores, mobile nativo y funciones aplazadas.

**Dependencias:** una semana de datos.  
**Evidencia:** postmortem sin culpa y roadmap aprobado.  
**Gate de salida:** operación normal, owners permanentes y deuda de lanzamiento visible.
