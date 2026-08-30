# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-022`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 18.1 — entitlements/limits/reserva/subscription state software-only`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `PREDECESSOR: NIGHT-WOZ-021 DONE / INTEGRATED — PR #67 merged. No repetir 021.`

### PRIMARY

1. Haz preflight GitHub vivo + duplicate-check. Si integration movió desde `3ad8f55a...`, reconcilia baseline antes de crear candidate.
2. REUSE-FIRST sobre el software integrado en #65 (checkout/catalog contract) y #67 (webhook durable/idempotent ledger). No dupliques billing primitives existentes.
3. Trabaja únicamente F3/18.1 software:
   - enforce limits/entitlements server-side **antes** de reservar recursos;
   - reserva/transacción anti-carreras con semántica atómica/fail-closed aplicable;
   - contrato server-side para Billing Portal/cancelación y estados de subscription, sin confiar en redirect/UI para conceder entitlement.
4. Si existe gap real, una sola rama/PR F3 mínima. Tests deben cubrir concurrencia/race, limit enforcement, estados relevantes y fail-closed.
5. No crear/usuar Stripe productivo, products/prices reales, credenciales, provider resources ni infraestructura pagada. No 18.2, 19.x, 20.x ni grace-period/business decisions.
6. Evidencia requerida: exact base/head, focused tests, DB/migration evidence si aplica, fresh applicable exact-head CI y race-check antes de merge cuando corresponda.
7. Reporta RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP. No auto-iniciar 18.2.

**Required evidence:** live baseline; REUSE-FIRST findings; branch/head/PR si aplica; tests de limits/race/subscription-state; exact-head CI; UNVERIFIED explícito; merge SHA solo si corresponde y está verde.  
**STOP:** decisión comercial no definida, necesidad Stripe/provider real, scope 18.2+, cambio destructivo/migration no justificable, CI rojo no atribuible o baseline no reconciliable.

### CI-FALLBACK

`NONE`

Reason: 18.2 comparte billing/PostgreSQL y depende de las semánticas de 18.1; 19/20 expanden área. No hay fallback independiente seguro preautorizado.

## RESULTADO PROCESADO — NIGHT-WOZ-021

- `STATUS: DONE / INTEGRATED — 17.2 SOFTWARE DONE / INTEGRATED`
- `BASE: 712b49b6689a31a47902dbe95e98622d001dab40`
- `EXACT_TESTED_HEAD: 27c2f30007a687a144be289a64ab986451f05c99`
- `PR: #67 MERGED`
- `CI: F3 17.2 33283532676 SUCCESS; D6 33283532664 SUCCESS; D7 33283532679 SUCCESS; temp-auth 33283532723 SUCCESS; Desktop Portability 33283532696 SUCCESS.`
- `MERGE/INTEGRATION: 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af.`
- `UNVERIFIED: Stripe productivo, 18.x, physical staging/prod — no reclamados.`
- `JOBS_ACTION: cerrar 17.2 software y emitir NIGHT-WOZ-022 para 18.1.`

## HISTORIAL COMPACTO

- `NIGHT-WOZ-022`: ASSIGNED — F3/18.1 software-only; CI-FALLBACK NONE.
- `NIGHT-WOZ-021`: DONE/INTEGRATED — PR #67 merged `3ad8f55a...`; 17.2 software closed.
- `NIGHT-WOZ-020`: PENDING/WAITING_CI — refreshed candidate `27c2f300...`.
- `NIGHT-WOZ-019`: PENDING/WAITING_CI — recovery verifier corrective.
- `NIGHT-WOZ-017`: PR #65 merged; 17.1 SOFTWARE DONE / INTEGRATED.
