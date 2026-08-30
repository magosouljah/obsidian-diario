# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción/operación software-only.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-033`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.1 — observability / alerts / runbook / kill-switch REUSE-FIRST gap map`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`
- `PREDECESSOR: NIGHT-WOZ-032 SUPERSEDED_BY_JOBS — no result observable before #63 changed integration baseline; do not execute 032 after receiving 033.`
- `HOLDING_ITEM_1: F2 / 13.1 / #70 frozen @ 5a99ebf2...; baseline stale + safe-write blocker.`
- `HOLDING_ITEM_2: F3 / 18.1 / #68 frozen @ 2a988ec2...; baseline stale + prior merge-execution blocker.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. No tocar #68/#70 ni reutilizar sus ramas.
2. Leer F3/20.1 literalmente y aplicar REUSE-FIRST sobre evidencia integrada: 5.2 observabilidad/alarms/on-call, #59 health/readiness, #61 promotion/rollback y artifacts actuales.
3. Construir mapa `requisito -> evidencia exacta -> cobertura -> gap` para:
   - logs/métricas/tracing/error reporting/retention;
   - alerts auth/API/DB/billing/provider/pool/queue/backup/release;
   - on-call/runbook/status/kill switches.
4. No marcar cobertura por naming parecido; evidencia literal/documentada/ejecutable.
5. Si una parte ya está satisfecha, citar paths/SHA/tests/runtime aplicable; no cerrar 20.1 completo salvo cobertura literal total.
6. Si aparece UN gap pequeño, independiente, software-only y safely writable, se autoriza una sola rama/PR nueva para ese gap. Preferir archivo/harness/test pequeño; no full-file destructive rewrite.
7. Provider/dashboard real, recursos pagados, secretos, DNS/status vendor o decisión RO => `PENDING_EXTERNAL`, sin falsear.
8. Si hay cambio: branch/head, changed-file scope, focused tests + fresh applicable exact-head CI. Sin cambio: gap map verificable basta.
9. Publicar handoff Issue #41, actualizar RESULTADO DEL TURNO aquí y STOP.

**STOP:** tocar #68/#70/F2/F4; full-file destructive write; provider/cost/secret action; scope creep; baseline race; CI rojo no atribuible.

### CI-FALLBACK

`NONE`

Reason: PRIMARY ya es read/audit-first y materialmente independiente; otro carril ampliaría scope.

## RESULTADO PROCESADO — NIGHT-WOZ-032

- `STATUS: NO_RESULT / SUPERSEDED_BY_JOBS`.
- Razón: #63 movió integration de `3ad8f55a...` a `02a40564...` antes de resultado observable. No ejecutar 032 tardíamente.

## HOLDING

- F2/13.1 / #70 @ `5a99ebf2...` — stale/frozen; safe-write tooling blocker.
- F3/18.1 / #68 @ `2a988ec2...` — stale/frozen; refresh/fresh CI obligatorio si se reactiva.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-033`: ASSIGNED — F3/20.1 observability gap map on live baseline.
- `NIGHT-WOZ-032`: NO_RESULT / SUPERSEDED_BY_JOBS due baseline move.
- `NIGHT-WOZ-031`: BLOCKED / SAFE_WRITE_TOOLING_LIMIT; #70 restored exactly.
- `NIGHT-WOZ-029`: attributed #70 corrective.
- `NIGHT-WOZ-025`: #68 exact-head green but merge execution blocked.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
