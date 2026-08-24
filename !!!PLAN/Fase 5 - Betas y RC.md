# Fase 5 — Dos betas, carga y release candidate

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 28 de septiembre–2 de octubre  
**Objetivo:** validar usuarios reales controlados, fallos y operación antes de congelar RC.

## Día 26 — 28 de septiembre — Beta 1 guiada

**Resultado:** al menos 12 testers representativos completan el guion en las tres plataformas.

### Tarea 26.1 [P1 · QA/Support] — Distribuir con seguridad

- [ ] Cohortes por Web/Windows/macOS/arquitectura/navegador; consentimiento y canal de soporte.
- [ ] Instalación, onboarding, importación, Review, player, edit, Trash y updater.
- [ ] Billing sandbox o compra real de owner únicamente; no cobrar testers por accidente.

### Tarea 26.2 [P1 · OP/RO] — Observar

- [ ] Correlacionar IDs de soporte sin exponer archivos/nombres/tokens.
- [ ] Revisar API/DB/Stripe/Telegram/bots y alertas durante la sesión.
- [ ] Clasificar P0 seguridad/datos, P1 core, P2 crecimiento y P3 polish.

**Dependencias:** beta candidate y soporte/on-call.  
**Evidencia:** tasa de finalización por flujo, tickets y dashboard.  
**Gate de salida:** 12 guiones completos o causa documentada; cualquier P0 detiene la beta.

## Día 27 — 29 de septiembre — Corrección y regresión Beta 1

**Resultado:** todos los P0/P1 de Beta 1 cerrados con test.

### Tarea 27.1 [P0/P1 · Owners] — Triage estricto

- [ ] Repro mínimo, causa raíz, fix, test y reviewer por hallazgo.
- [ ] No combinar refactors o delight no relacionados.
- [ ] Data repair script solo con dry-run, backup y aprobación.

### Tarea 27.2 [P1 · QA] — Revalidar

- [ ] Suites afectadas y regresión completa del candidato.
- [ ] Repro en el dispositivo/navegador original.
- [ ] Confirmar que fix no cambia legal, billing o formato sin migración.

**Dependencias:** evidencia Beta 1.  
**Evidencia:** issue→PR→test→retest enlazado.  
**Gate de salida:** 0 P0/P1 abierto; P2 tiene owner o aceptación explícita antes de crecimiento.

## Día 28 — 30 de septiembre — Carga y game day

**Resultado:** BeatGaler degrada de forma controlada y se recupera.

### Tarea 28.1 [P1 · OP/BE/QA] — Carga

- [ ] Cuenta limpia, refresh, lease, import/upload, playback Range, index commits y webhooks al 2× del pico propuesto.
- [ ] Archivos grandes dentro de límites; queues/admission y saturación controlada.
- [ ] Comparar pool actual vs capacidad requerida; agregar bots solo si la métrica lo exige.

### Tarea 28.2 [P0/P1 · OP] — Fallas deliberadas

- [ ] API/DB/Stripe/Telegram/bot/master/SSE caídos o lentos; estado pool corrupto.
- [ ] Kill switches, fail closed, retry bounded, alert, status y recovery.
- [ ] Restore de backup y rollback de app/deploy durante el ejercicio.

**Dependencias:** monitoring y runbooks.  
**Evidencia:** load/game-day report con timeline y acciones.  
**Gate de salida:** sin pérdida/cross-tenant; RPO/RTO y alert delivery dentro de targets aprobados.

## Día 29 — 1 de octubre — Beta 2 no guiada

**Resultado:** testers nuevos completan sin ayuda los flujos de lanzamiento.

### Tarea 29.1 [P1 · QA/DL] — Usabilidad real

- [ ] Al menos 8 testers nuevos, distribuidos por plataformas; primero observación, luego entrevista.
- [ ] Medir tiempo/abandono/error de signup→first beat→play→edit→restore.
- [ ] Probar recuperación, delete/export, billing/portal y soporte.

### Tarea 29.2 [P1 · RO/Owners] — Cierre

- [ ] P0/P1 tienen fix o el release se mueve; no se “aceptan” por fecha.
- [ ] P2 que afecta crecimiento tiene compensación/limitación y owner.
- [ ] Validar copy final, download page, changelog y known limitations.

**Dependencias:** Día 28 exitoso.  
**Evidencia:** guiones, métricas, tickets y aceptación por plataforma.  
**Gate de salida:** 0 P0/P1; core-flow completion objetivo ≥90% sin asistencia para cohorte propuesta.

## Día 30 — 2 de octubre — RC inmutable

**Resultado:** `1.0.0-rc.1` queda congelado y reproducible.

### Tarea 30.1 [P0 · RO/OP/DE] — Cortar RC

- [ ] Tag protegido y firmado; generar todos los artefactos desde el mismo SHA.
- [ ] SBOM, checksums, signatures, notarization ticket, migrations y release notes.
- [ ] Promover a staging; no reconstruir manualmente para producción.

### Tarea 30.2 [P0/P1 · QA/Security/LF] — Gate formal

- [ ] Suite completa, advisory/secret/license scan y revisión de diferencias desde beta.
- [ ] Security, legal, payments, support, recovery y platform sign-offs.
- [ ] Abrir change freeze: solo hotfix P0/P1 con nueva RC y repetición de gates afectados.

**Dependencias:** dos betas y game day.  
**Evidencia:** release dossier firmado.  
**Gate de salida:** RC inmutable, 0 P0/P1 y 100% de confirmaciones launch-critical con evidencia.
