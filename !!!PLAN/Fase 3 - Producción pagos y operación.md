# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 104:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios reales siguen abiertos.
- 19.1 infraestructura pública principal `PROVEN_OWNER_RUNTIME`; functional `Loading Galer` pertenece F2. Legal/public-route/support/OAuth/status tails parciales.
- 19.2 #76 reusable pero stale/13+ y bloqueado por falta de refresh history-preserving.
- 20.1 software observability integrado; external observability tails abiertos.
- #78 capacity harness integrado; #83 durable waitlist OPEN/DRAFT tooling-blocked; runtime 160 UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`
Software reconciliation + durable exception queue está probado. 3DS, rejection, late payment, renewal failure, cancel E2E, plan changes, refund, provider webhooks/financial outcomes y full sandbox reconciliation permanecen `UNVERIFIED_EXTERNAL`. Owner billing policy no sustituye provider/runtime PASS.

## 19.1 — `[ 🟡 ] PUBLIC INFRA PROVEN / EXTERNAL TAILS OPEN`
Owner Issue #41 `5485984669` mantiene probado `/web-health`, auth-health, www→apex y TLS apex/www. PR #85 sigue external/owner-owned y no se duplica.

**Nuevo candidate observado CYCLE 104: PR #87** `F0/0.6: publish security.txt and status surface`:
- OPEN/Ready/mergeable;
- exact base `816f946c...`;
- head `d5d129c578355ca2ff6399bd2e6ec752c9f81618`;
- software scope declara `.well-known/security.txt`, public status page, Nginx/bootstrap support y expiry guard;
- body declara `status.beatgaler.com` DNS + post-merge/deploy runtime **UNVERIFIED**.

No se promueve cierre 19.1 desde #87. `NIGHT-WOZ-103` puede inspeccionarlo READ-ONLY únicamente como CI-FALLBACK mientras #86 espera CI; no mutar/mergear #87 este ciclo. Support/mail/OAuth/public legal routes/status runtime siguen requiriendo evidencia aplicable.

## 19.2 — `[ 🟡 ] BLOCKED ON REFRESH-CAPABLE EXECUTION SURFACE`
PR #76 @ `36d218609cf2488997755312fa2dafd0a019d070` permanece stale; 13+ contradice v1 canónico **18+**, Settings copy requiere reconciliación. `NIGHT-WOZ-100` ya probó que la superficie soportada no puede hacer refresh history-preserving; no repetir hasta cambio material.

## 20.1 — `[x] SOFTWARE DONE / INTEGRATED`
Structured redacted events, counters, routes, kill switches, tests/runbook integrados por #75. External provider/on-call/status/retention proof no se infiere.

## 20.2 — `[ 🟡 ] RUNTIME UNVERIFIED`
#78 harness integrado; expected peak 80. Falta runtime aplicable a **160 concurrent users**, latency/error/queue/recovery, safety margin. #83 @ `803b2143...` sigue OPEN/DRAFT/tooling-blocked. Integrarlo tampoco cerraría runtime 160.

**Principio:** no falsear provider, capacity, payments, DNS, legal review, deployment o staging sin evidencia externa/productiva.
