# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción/operación software-only.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-034`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.1 — software observability contract A: event/metric/alert taxonomy`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`
- `PREDECESSOR: NIGHT-WOZ-033 DONE / AUDIT_ONLY — processed by JOBS; do not rerun.`
- `HOLDING_ITEM_1: F2 / 13.1 / #70 frozen @ 5a99ebf2...; baseline stale + safe-write blocker.`
- `HOLDING_ITEM_2: F3 / 18.1 / #68 frozen @ 2a988ec2...; baseline stale + prior merge-execution blocker.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check sobre `02a40564...`. No tocar #68/#70 ni reutilizar sus ramas.
2. REUSE-FIRST del gap map de `NIGHT-WOZ-033` y de evidencia integrada (`runtime-operability`, backup readiness, promotion/rollback). No crear un segundo sistema de observabilidad.
3. Scope exacto de este turno: cerrar únicamente el **contrato software** de taxonomía operativa para eventos/métricas/alerts. Debe existir una fuente canónica pequeña que permita mapear, como mínimo, auth/API/DB/billing/provider/pool/queue/backup/release a nombre/severidad/señal y referencia de respuesta/runbook cuando aplique.
4. Reutilizar la taxonomía `backup.failure` y cualquier naming ya existente; no renombrar ceremonialmente superficies estables.
5. Preferir un módulo/contract/test pequeño y aditivo. No hacer broad logging rewrite, tracing backend, dashboard, alert delivery real, status vendor, on-call schedule o retention provider.
6. Si el gap puede resolverse sin código mediante evidencia ya existente, documenta literal coverage y STOP; no abras PR ceremonial.
7. Si requiere cambio, solo proceder si existe superficie de escritura segura. Evidencia: exact base/head, changed-file scope, focused contract tests y fresh applicable exact-head CI.
8. No marcar 20.1 completo. `metrics backend`, tracing, external error reporting, configured alert delivery, dashboards, retention, on-call y public status continúan UNVERIFIED/PENDING_EXTERNAL salvo evidencia real.
9. Publicar handoff en Issue #41, escribir RESULTADO DEL TURNO aquí y STOP.

**STOP:** full-file destructive write; scope crece a provider/dashboard/tracing/status/on-call; tocar #68/#70/F2/F4; coste/secret action; baseline race; CI rojo no atribuible.

### CI-FALLBACK

`NONE`

Reason: el PRIMARY ya es un slice software autónomo y acotado; otro carril ampliaría 20.1 o solaparía owners.

## RESULTADO PROCESADO — NIGHT-WOZ-033

- `STATUS: DONE / AUDIT_ONLY — 20.1 remains OPEN`.
- Baseline exacto `02a40564d85284a119281ff79995c9b9bcb5e833`; sin branch/PR/código.
- Evidencia reutilizada: `cloud-server/runtime-operability.js`, `cloud-server/server.js`, `cloud-server/deployment-promotion-contract.mjs`, `cloud-server/d10-backup-readiness-contract.mjs`.
- Gap map factual:
  - logs = PARTIAL; structured service-wide production logging/retention no demostrado;
  - metrics = GAP;
  - tracing = GAP;
  - error reporting = PARTIAL/GAP;
  - retention = PARTIAL/EXTERNAL;
  - alert routing matrix auth/API/DB/billing/provider/pool/queue/release = GAP; backup alert = PARTIAL SOFTWARE CONTRACT;
  - on-call = GAP/PENDING_EXTERNAL;
  - runbook = PARTIAL;
  - public status = GAP/PENDING_EXTERNAL;
  - kill switches = GAP.
- No se identificó una única pieza diminuta que cerrara 20.1 completo honestamente.
- Handoff Issue #41 `5468767913`.
- Recomendación procesada por JOBS: separar software contract de external provider/dashboard/on-call/status/retention proof.

## RESULTADO PROCESADO — NIGHT-WOZ-032

- `STATUS: NO_RESULT / SUPERSEDED_BY_JOBS` por movimiento de baseline antes de resultado observable.

## HOLDING

- F2/13.1 / #70 @ `5a99ebf2...` — stale/frozen; safe-write tooling blocker.
- F3/18.1 / #68 @ `2a988ec2...` — stale/frozen; refresh/fresh CI obligatorio si se reactiva.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-034`: ASSIGNED — F3/20.1 software observability contract A.
- `NIGHT-WOZ-033`: DONE / AUDIT_ONLY — 20.1 gap map; no code/PR; remains OPEN.
- `NIGHT-WOZ-032`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-031`: BLOCKED / SAFE_WRITE_TOOLING_LIMIT; #70 restored exactly.
- `NIGHT-WOZ-029`: attributed #70 corrective.
- `NIGHT-WOZ-025`: #68 exact-head green but merge execution blocked.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
