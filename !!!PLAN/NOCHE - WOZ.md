# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — billing/entitlements software-only.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-039`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 18.2 — reconciliation + exception-queue software contract`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `PREDECESSOR: NIGHT-WOZ-038 NOT_PROCESSED / SUPERSEDED_BY_JOBS — no result/handoff observable at CYCLE 040; no baseline movement, mission retained because it remains highest dependency-ready F3 work.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check y releer 18.1 ya integrado.
2. REUSE-FIRST: auditar primitives actuales de reconciliation, webhook/event-ledger, subscription state, retry/idempotency y exception handling.
3. No crear recursos Stripe, credenciales, productos/precios, checkout real ni infraestructura. No inventar grace periods/refund/upgrade/downgrade policy.
4. Si reconciliation + exception queue ya están literalmente satisfechas con evidencia, audit/handoff sin PR ceremonial.
5. Si hay gap interno, implementar solo slice mínimo software-only: detectar divergencia provider↔BeatGaler; excepción durable/idempotente; retry/reconcile seguro; fail-closed; nunca entitlement por redirect/session.
6. Focused tests: replay/idempotencia, divergence, exception/retry y no-grant ambiguo/incompleto.
7. Fresh applicable exact-head CI para cualquier nuevo head.
8. No cerrar 18.2 completo mientras queden casos de negocio/proveedor literales; separar `SOFTWARE DONE` de tails externos/RO.
9. No iniciar 19.x/20.x ni tomar #69/#70/#71/#72.
10. Escribir RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**STOP:** decisión RO/proveedor/credencial; scope drift; baseline race; evidencia insuficiente; CI rojo no atribuible.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO PROCESADO — NIGHT-WOZ-038

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No RESULTADO DEL TURNO/handoff observable al preflight CYCLE 040.
- GitHub live baseline no cambió después de #68; 18.2 sigue dependency-ready y distinto de AAA/BBB, por eso la misión se reemite como WOZ039.

## ÚLTIMO RESULTADO MATERIAL

- `NIGHT-WOZ-037: DONE / INTEGRATED`.
- PR #68 exact head `68adaad4a5b1b2b50ba192c1b58325cbba0472e3` merged como `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- F3/18.1 `[x] SOFTWARE DONE / INTEGRATED`.

## HOLDING

- F3/20.1 gap map WOZ033 válido, unassigned.
- F2/#70 stale/frozen; fuera de scope.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-039`: ASSIGNED — F3/18.2 reconciliation/exception queue.
- `NIGHT-WOZ-038`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-037`: DONE/INTEGRATED — #68 merge `a9d35a3d...`.
- `NIGHT-WOZ-033`: DONE/AUDIT_ONLY — 20.1 gap map.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
