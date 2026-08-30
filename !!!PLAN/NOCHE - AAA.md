# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área:** Desktop product-auth corrective.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-038`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 blocker / Desktop product-auth — token/session persistence`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `INPUT_EVIDENCE: PR #71 / BBB034 product finding — Desktop login no persistió beatgaler:account-session:v1`
- `PREDECESSOR: NIGHT-AAA-037 NOT_PROCESSED / SUPERSEDED_BY_JOBS — no resultado/handoff observable al CYCLE 040; no ejecutar 037 después de recibir 038.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check; integration debe reconciliarse antes de mutar.
2. REUSE-FIRST: tomar el PRODUCT_FINDING de #71 y demostrar causa raíz en código productivo auth/frontend/platform y contrato `AccountGate.storeSession()`.
3. No tocar PR/branch/files de #71; queda como regression proof F4.
4. Solo con causa raíz demostrada, aplicar corrective mínimo en una rama/PR AAA nueva desde baseline vivo. Sin refactor amplio ni cambio de contrato auth/security.
5. Evidencia obligatoria: fail-before/pass-after o equivalente literal; sesión/token persistido tras login Desktop; no regresión Web/AccountGate; fresh applicable exact-head CI.
6. Si integra, handoff para devolver #71 a BBB mediante asignación JOBS posterior; no promover matrix desde AAA.
7. No tocar #69/#70, Review/#72, F3, signing/notarization, infra/provider secrets ni otras filas 25.1.
8. Escribir RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**STOP:** finding no reproducible; causa raíz no demostrable; cambio de contrato/seguridad no autorizado; scope creep; baseline race; CI rojo no atribuible.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO PROCESADO — NIGHT-AAA-037

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No RESULTADO DEL TURNO ni handoff observable en ledger/Issue #41 al preflight CYCLE 040.
- La misión sigue siendo críticamente válida por el PRODUCT_FINDING de #71 y se reemite como AAA038 sobre el mismo baseline vivo.

## HOLDING

- F2/12.1 cold/warm real: runtime navegador ejecutable faltante.
- F2/13.1 Web #69: coordinator probado; wiring/refresh pendientes y candidate stale.
- F2/13.1 server #70: frozen por safe-write + stale baseline.

## HISTORIAL COMPACTO

- `NIGHT-AAA-038`: ASSIGNED — product-auth token/session persistence corrective.
- `NIGHT-AAA-037`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-AAA-036`: NOT_PROCESSED / SUPERSEDED_BY_JOBS por baseline movement.
- `NIGHT-AAA-032`: PENDING / STOP_RUNTIME_UNAVAILABLE.
- `NIGHT-AAA-031`: PENDING / STOP_WRITE_SURFACE.
- `NIGHT-AAA-027`: #69 created.
