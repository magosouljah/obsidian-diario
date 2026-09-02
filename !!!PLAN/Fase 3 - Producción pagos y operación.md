# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE154:** `integration-v0.8.0-alpha.1 @ c4e203cf5e44cf93c0c017c0120f097473fe91b2`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios reales abiertos.
- 19.1 infraestructura pública principal `PROVEN_OWNER_RUNTIME`; external/provider tails parciales.
- 19.2 legal implementation sustantiva abierta: 12 P0 + 14 P1 + P2/P3 + UNVERIFIED; v1 canónico = **18+**.
- 20.1 software observability integrado; external observability tails abiertos.
- #78 capacity harness integrado; #83 durable waitlist OPEN/DRAFT; runtime160 UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`

Software reconciliation + durable exception queue probado. 3DS, rejection, late payment, renewal failure, cancel E2E, plan changes, refund, provider webhooks/financial outcomes y full sandbox reconciliation = `UNVERIFIED_EXTERNAL`.

Para alpha 3–5 cuentas sin cobros, 1.7 debe clasificar explícitamente `RO_EXCLUDE_CANDIDATE` o `MUST_CLOSE`; no se infiere exclusión. BBB149 puede usar un fallback READ-ONLY para inventario solo durante espera externa real de su recent-reauth PRIMARY; no ejecuta pagos/provider mutation ni decide exclusión.

## 19.1 — `[ 🟡 ] PUBLIC SOFTWARE/RUNTIME IMPROVED / EXACT SOURCE BINDING OPEN`

#98 ya está **integrado** en `c4e203cf...`, con Required CI exact-head SUCCESS. Su body reporta clean production deployment, public/local health PASS, library materialization, artwork y playback success. AAA150 debe clasificar si esa evidencia puede ligarse a exact deployment/source antes de cerrar F2/12.1 o promover más allá de lo literal.

## 19.2 — `[ 🟡 ] LEGAL IMPLEMENTATION OPEN / REVIEW TASK COMPLETE`

PR #76 sigue stale; 13+ contradice v1 **18+**. F0/0.8 `[x]` significa solo AI-assisted review activity completada por excepción RO, no attorney review/compliance. Los 12 P0 + 14 P1 y demás backlog siguen gates de implementation/release y 1.7 debe clasificar alpha applicability sin declararlos resueltos.

## 20.1 — `[x] SOFTWARE DONE / INTEGRATED`

Structured redacted events, counters, routes, kill switches, tests/runbook integrados. External provider/on-call/status/retention proof no se infiere.

## 20.2 — `[ 🟡 ] RUNTIME UNVERIFIED`

#78 harness integrado; expected peak 80. Falta runtime aplicable a **160 concurrent users**, latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin. #83 sigue OPEN/DRAFT/stale. Para alpha 3–5 cuentas, 1.7 debe clasificar explícitamente aplicabilidad.

## Cross-phase security tail

PR #89 sigue OPEN @ `daf87da6...`, stale base `816f946c...`, security run `33454881387` FAILURE. CYCLE154 no le asigna mutation owner; WOZ153 solo puede inventariarlo READ-ONLY como fallback mientras Issue #97 espera externamente.

**Principio:** no falsear provider, capacity, payments, DNS, deployment, staging, legal compliance ni independent counsel review sin evidencia aplicable.
