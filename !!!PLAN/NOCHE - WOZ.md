# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — billing/entitlements software-only.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-038`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 18.2 — reconciliation + exception-queue software contract`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `PREDECESSOR: NIGHT-WOZ-037 DONE / INTEGRATED — PR #68 merge a9d35a3d...`
- `CI-FALLBACK: NONE`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check y lectura de 18.1 ya integrado.
2. REUSE-FIRST: auditar primitives existentes para Stripe↔BeatGaler reconciliation, webhook/event ledger, subscription state, retry/idempotency y exception handling.
3. No crear recursos Stripe, credenciales, productos/precios, checkout real ni tocar infraestructura. No inventar grace periods ni decisiones de refund/upgrade/downgrade.
4. Si el requisito software de reconciliación + cola de excepciones ya existe literalmente y tiene evidencia suficiente, producir audit/handoff sin PR ceremonial.
5. Si existe gap literal interno, implementar solo el slice mínimo software-only para: detectar divergencia entre estado proveedor y autoridad BeatGaler; registrar excepción durable/idempotente; permitir retry/reconcile seguro sin conceder entitlement por redirect/session; conservar fail-closed.
6. Tests focused deben cubrir al menos: replay/idempotencia, provider state divergence, excepción/retry y no-grant ante dato incompleto/ambiguo.
7. Fresh applicable exact-head CI para cualquier nuevo head. No marcar 18.2 `[x]` si siguen abiertos casos de negocio/proveedor requeridos.
8. No iniciar 19.x/20.x ni tomar #70/#69/#71.
9. Escribir RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**STOP:** requiere decisión RO de grace/refund/upgrade/downgrade; requiere Stripe productivo/credenciales; scope drift; baseline race; evidencia insuficiente para claim; CI rojo no atribuible.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO PROCESADO — NIGHT-WOZ-037

### PRIMARY

- `STATUS: DONE / INTEGRATED`.
- PR #68 `woz/night-18.1-entitlements-reservation @ 68adaad4a5b1b2b50ba192c1b58325cbba0472e3` MERGED.
- Merge SHA / new integration HEAD: `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- Parents: `02a40564...` + `68adaad4...`; tree `166941bf...`.
- Exact-head evidence reused: F3 18.1, D6, D7, productive temp-auth and Desktop Portability SUCCESS; Upgrade 21.2 SKIPPED/non-applicable; zero failure/pending.
- Scope: 4 files / +178 -0; no new code in merge turn.
- Issue #41 handoff `5469367978`.
- `18.1` puede procesarse como `[x] SOFTWARE DONE / INTEGRATED`; Stripe/provider real y 18.2 permanecen aparte.

### CI-FALLBACK

`STATUS: NOT_RUN / NONE`.

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-037`  
`TURN_STATUS: DONE`  
`HEAD_AFTER: a9d35a3d69dd9127029fb851d189f9bd3079d03b`  
`PR: #68 MERGED`

## HOLDING

- F3/20.1 gap map WOZ033 — válido, unassigned.
- F2/#70 — stale/frozen; fuera de scope.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-038`: ASSIGNED — F3/18.2 reconciliation/exception-queue software-only.
- `NIGHT-WOZ-037`: DONE / INTEGRATED — #68 merge `a9d35a3d...`.
- `NIGHT-WOZ-036`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-033`: DONE / AUDIT_ONLY — 20.1 gap map.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
