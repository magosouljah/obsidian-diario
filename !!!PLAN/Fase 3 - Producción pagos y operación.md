# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 108:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios reales siguen abiertos.
- 19.1 infraestructura pública principal `PROVEN_OWNER_RUNTIME`; #87 security/status software slice integrated, pero DNS/SAN/deploy/public runtime/support/OAuth/legal tails siguen parciales.
- 19.2 #76 reusable pero stale/13+ y bloqueado por falta de refresh history-preserving; v1 canónico = **18+**. **F0/0.8 review activity está `[x]` bajo excepción AI-assisted RO-approved, pero 19.2 y el backlog legal sustantivo permanecen abiertos: 12 P0 + 14 P1 + P2/P3 + UNVERIFIED.**
- 20.1 software observability integrado; external observability tails abiertos.
- #78 capacity harness integrado; #83 durable waitlist OPEN/DRAFT; runtime 160 UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`
Software reconciliation + durable exception queue está probado. 3DS, rejection, late payment, renewal failure, cancel E2E, plan changes, refund, provider webhooks/financial outcomes y full sandbox reconciliation permanecen `UNVERIFIED_EXTERNAL`. Owner billing policy no sustituye provider/runtime PASS.

## 19.1 — `[ 🟡 ] PUBLIC SOFTWARE IMPROVED / EXTERNAL TAILS OPEN`
Owner Issue #41 `5485984669` mantiene probado `/web-health`, auth-health, www→apex y TLS apex/www. PR #85 sigue external/owner-owned y no se duplica.

PR #87 public security/status software slice quedó integrado como `38517c8065063206fed530028e4e8d20208f3807`; promoción aceptada solo para software implementation. Esto no demuestra status DNS, certificate SAN, production deploy, public runtime, support mailbox, OAuth production callback ni legal implementation/compliance.

## 19.2 — `[ 🟡 ] LEGAL IMPLEMENTATION OPEN / REVIEW TASK COMPLETE`
PR #76 @ `36d218609cf2488997755312fa2dafd0a019d070` permanece stale; 13+ contradice v1 canónico **18+**, Settings copy requiere reconciliación. No repetir hasta cambio material de superficie/tooling y owner explícito.

**Administrative review state:** F0/0.8 is `[x]` only because RO explicitly replaced the independent-counsel review requirement for that review gate with the AI-assisted audit completed on **2026-08-31** and accepted the residual risk of deferring counsel. This is not attorney review and is not a compliance claim.

**Canonical legal backlog/evidence:** [`Legal launch review - AI-assisted 2026-08-31.md`](./Legal%20launch%20review%20-%20AI-assisted%202026-08-31.md).

The audit's **12 P0 and 14 P1 remain open release/implementation gates**. P2/P3 and all `UNVERIFIED` items remain open backlog/risk. The global `NO-GO` is unchanged, and `Gates - Publicación y contingencias.md` still prohibits release while any applicable P0/P1 remains.

## 20.1 — `[x] SOFTWARE DONE / INTEGRATED`
Structured redacted events, counters, routes, kill switches, tests/runbook integrados por #75. External provider/on-call/status/retention proof no se infiere.

## 20.2 — `[ 🟡 ] RUNTIME UNVERIFIED`
#78 harness integrado; expected peak 80. Falta runtime aplicable a **160 concurrent users**, latency/error/queue/recovery, safety margin. #83 @ `803b2143...` sigue OPEN/DRAFT y stale. Integrarlo tampoco cerraría runtime 160.

## Cross-phase security tail relevante
PR #89 F0/0.9 contiene P1 DNS-rebinding SSRF corrective + audit AI-assisted. **Owner CYCLE 108: `NIGHT-WOZ-107` bajo F0.** #89 sigue stale; old-head green CI no sustituye refresh/exact-head. Si se integra, solo reduce riesgo software; no sustituye provider/runtime/public-operation evidence de F3.

**Principio:** no falsear provider, capacity, payments, DNS, deployment, staging, legal compliance ni independent counsel review sin evidencia externa/productiva.
