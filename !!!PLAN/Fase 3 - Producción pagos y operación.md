# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE118:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3` al preflight JOBS.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios reales siguen abiertos.
- 19.1 infraestructura pública principal `PROVEN_OWNER_RUNTIME`; #87 security/status software integrated; external/provider tails aplicables siguen parciales. #90 software/readiness de OAuth rotation está integrado y 0.20 quedó cerrado por owner evidence, sin registrar secretos.
- 19.2 #76 reusable pero stale/13+; v1 canónico = **18+**. F0/0.8 review activity está `[x]` bajo excepción AI-assisted RO-approved, pero 19.2/backlog legal sustantivo permanece abierto: 12 P0 + 14 P1 + P2/P3 + UNVERIFIED.
- 20.1 software observability integrado; external observability tails abiertos.
- #78 capacity harness integrado; #83 durable waitlist OPEN/DRAFT; runtime160 UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`

Software reconciliation + durable exception queue está probado. 3DS, rejection, late payment, renewal failure, cancel E2E, plan changes, refund, provider webhooks/financial outcomes y full sandbox reconciliation permanecen `UNVERIFIED_EXTERNAL`.

Para una alpha 3–5 cuentas sin cobros, F1/1.7 debe clasificar explícitamente este gate como `EXCLUDED_FROM_ALPHA` o `IN_ALPHA`; no se infiere exclusión automáticamente y release público sigue sujeto al gate completo.

## 19.1 — `[ 🟡 ] PUBLIC SOFTWARE IMPROVED / EXTERNAL TAILS OPEN`

Owner evidence mantiene `/web-health`, auth-health, www→apex y TLS probados en evidencia previa aplicable. #87 software slice está integrado; #88 technical signing seam y #90 OAuth readiness software están integrados. Ninguno cierra por sí solo F3 ni sustituye deploy/runtime actual de F2/12.1 post-#95.

## 19.2 — `[ 🟡 ] LEGAL IMPLEMENTATION OPEN / REVIEW TASK COMPLETE`

PR #76 @ `36d218609cf2488997755312fa2dafd0a019d070` permanece stale; 13+ contradice v1 **18+** y Settings copy requiere reconciliación. No repetir hasta cambio material de surface/tooling y owner explícito.

F0/0.8 es `[x]` solo porque RO sustituyó independent-counsel review por AI-assisted audit del `2026-08-31` y aceptó riesgo residual. No es attorney review ni compliance. Evidence canónica: `Legal launch review - AI-assisted 2026-08-31.md`. Sus **12 P0 + 14 P1** siguen release/implementation gates; P2/P3 y `UNVERIFIED` siguen backlog/risk. Global `NO-GO` no cambia.

## 20.1 — `[x] SOFTWARE DONE / INTEGRATED`

Structured redacted events, counters, routes, kill switches, tests/runbook integrados por #75. External provider/on-call/status/retention proof no se infiere.

## 20.2 — `[ 🟡 ] RUNTIME UNVERIFIED`

#78 harness integrado; expected peak 80. Falta runtime aplicable a **160 concurrent users**, latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin. #83 @ `803b2143...` sigue OPEN/DRAFT y stale. Integrarlo tampoco cerraría runtime160.

Para alpha 3–5 cuentas, F1/1.7 debe clasificar 20.2 explícitamente; runtime160 es release/scale evidence y no se fabrica como prerequisito representativo de una alpha pequeña salvo decisión/gate explícito.

## Cross-phase security tail

PR #89 F0/0.9 contiene P1 DNS-rebinding SSRF corrective + audit AI-assisted. **Owner CYCLE118: `NIGHT-WOZ-117` bajo F0.** #89 sigue OPEN @ `daf87da6...`, base registrada `816f946c...`, `mergeable=false` contra live `43fdf70e...`; old-head green no sustituye refresh/exact-head. WOZ117 posee la única conditional integration lane sobre #89 y solo puede mergear tras refresh bounded, CI exact-head verde y race-check. Si se integra, reduce riesgo software pero no sustituye provider/payment/capacity/legal evidence de F3.

**Principio:** no falsear provider, capacity, payments, DNS, deployment, staging, legal compliance ni independent counsel review sin evidencia aplicable.
