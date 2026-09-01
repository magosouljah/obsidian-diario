# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 106:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios reales siguen abiertos.
- 19.1 infraestructura pública principal `PROVEN_OWNER_RUNTIME`; #87 security/status **software slice integrated**, pero DNS/SAN/deploy/public runtime/support/OAuth/legal tails siguen parciales.
- 19.2 #76 reusable pero stale/13+ y bloqueado por falta de refresh history-preserving.
- 20.1 software observability integrado; external observability tails abiertos.
- #78 capacity harness integrado; #83 durable waitlist OPEN/DRAFT; runtime 160 UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`
Software reconciliation + durable exception queue está probado. 3DS, rejection, late payment, renewal failure, cancel E2E, plan changes, refund, provider webhooks/financial outcomes y full sandbox reconciliation permanecen `UNVERIFIED_EXTERNAL`. Owner billing policy no sustituye provider/runtime PASS.

## 19.1 — `[ 🟡 ] PUBLIC SOFTWARE IMPROVED / EXTERNAL TAILS OPEN`
Owner Issue #41 `5485984669` mantiene probado `/web-health`, auth-health, www→apex y TLS apex/www. PR #85 sigue external/owner-owned y no se duplica.

PR #87 `F0/0.6: publish security.txt and status surface` quedó integrado por `NIGHT-WOZ-104`:
- exact candidate head `ba0d7b689e587da42cc8105b22d0ed0c206bc064`;
- exact base `b85723e1b3016d24bdb943393e796ccdb744247d`;
- merge `38517c8065063206fed530028e4e8d20208f3807`;
- exact parents `b85723e...` + `ba0d7b...`;
- applicable exact-head CI observado SUCCESS.

**Promoción aceptada:** public security/status **software implementation slice PASS/INTEGRATED**. Esto no demuestra status DNS, certificate SAN, production deploy, public runtime, support mailbox, OAuth production callback ni independent legal review.

## 19.2 — `[ 🟡 ] BLOCKED ON REFRESH-CAPABLE EXECUTION SURFACE`
PR #76 @ `36d218609cf2488997755312fa2dafd0a019d070` permanece stale; 13+ contradice v1 canónico **18+**, Settings copy requiere reconciliación. No repetir hasta cambio material de superficie/tooling y owner explícito.

## 20.1 — `[x] SOFTWARE DONE / INTEGRATED`
Structured redacted events, counters, routes, kill switches, tests/runbook integrados por #75. External provider/on-call/status/retention proof no se infiere.

## 20.2 — `[ 🟡 ] RUNTIME UNVERIFIED`
#78 harness integrado; expected peak 80. Falta runtime aplicable a **160 concurrent users**, latency/error/queue/recovery, safety margin. #83 @ `803b2143...` sigue OPEN/DRAFT. Integrarlo tampoco cerraría runtime 160.

## Cross-phase security tail relevante
PR #89 F0/0.9 contiene un P1 DNS-rebinding SSRF corrective y audit AI-assisted. `NIGHT-WOZ-105` lo owns bajo F0; F3 no adquiere ownership del PR. Si se integra, solo reduce riesgo software; no sustituye provider/runtime/public-operation evidence de esta fase.

**Principio:** no falsear provider, capacity, payments, DNS, legal review, deployment o staging sin evidencia externa/productiva.
