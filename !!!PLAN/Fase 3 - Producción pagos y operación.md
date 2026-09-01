# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE134:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3` al preflight JOBS.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios reales siguen abiertos.
- 19.1 infraestructura pública principal `PROVEN_OWNER_RUNTIME`; external/provider tails aplicables siguen parciales.
- 19.2 #76 reusable pero stale/13+; v1 canónico = **18+**. F0/0.8 review activity `[x]` bajo excepción AI-assisted RO-approved, pero 19.2/backlog legal sustantivo permanece abierto: 12 P0 + 14 P1 + P2/P3 + UNVERIFIED.
- 20.1 software observability integrado; external observability tails abiertos.
- #78 capacity harness integrado; #83 durable waitlist OPEN/DRAFT; runtime160 UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`

Software reconciliation + durable exception queue está probado. 3DS, rejection, late payment, renewal failure, cancel E2E, plan changes, refund, provider webhooks/financial outcomes y full sandbox reconciliation permanecen `UNVERIFIED_EXTERNAL`.

Para una alpha 3–5 cuentas sin cobros, F1/1.7 debe clasificar explícitamente este gate como `RO_EXCLUDE_CANDIDATE` o `MUST_CLOSE`; no se infiere exclusión automáticamente. Owner de clasificación CYCLE134: `NIGHT-AAA-130` READ-ONLY. Release público sigue sujeto al gate completo.

## 19.1 — `[ 🟡 ] PUBLIC SOFTWARE IMPROVED / EXTERNAL TAILS OPEN`

Owner evidence previo mantiene `/web-health`, auth-health, www→apex y TLS probados en evidencia aplicable. #87 software slice, #88 technical signing seam y #90 OAuth readiness están integrados. Ninguno cierra por sí solo F3 ni sustituye deploy/runtime actual de F2/12.1 post-#95.

## 19.2 — `[ 🟡 ] LEGAL IMPLEMENTATION OPEN / REVIEW TASK COMPLETE`

PR #76 @ `36d218609cf2488997755312fa2dafd0a019d070` permanece stale; 13+ contradice v1 **18+** y Settings copy requiere reconciliación. No repetir hasta cambio material de surface/tooling y owner explícito.

F0/0.8 es `[x]` solo porque RO sustituyó independent-counsel review por AI-assisted audit del `2026-08-31` y aceptó riesgo residual. No es attorney review ni compliance. Sus **12 P0 + 14 P1** siguen release/implementation gates; P2/P3 y `UNVERIFIED` siguen backlog/risk. F1/1.7 debe clasificar aplicabilidad al alpha sin declararlos resueltos.

## 20.1 — `[x] SOFTWARE DONE / INTEGRATED`

Structured redacted events, counters, routes, kill switches, tests/runbook integrados por #75. External provider/on-call/status/retention proof no se infiere.

## 20.2 — `[ 🟡 ] RUNTIME UNVERIFIED`

#78 harness integrado; expected peak 80. Falta runtime aplicable a **160 concurrent users**, latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin. #83 @ `803b2143...` sigue OPEN/DRAFT y stale. Integrarlo tampoco cerraría runtime160.

Para alpha 3–5 cuentas, F1/1.7 debe clasificar explícitamente 20.2; no se fabrica como prerequisito representativo ni se excluye sin decisión RO.

## Cross-phase security tail

PR #89 F0/0.9 contiene P1 DNS-rebinding SSRF corrective + audit AI-assisted. **Owner CYCLE134: `NIGHT-WOZ-133` bajo F0.** #89 sigue OPEN @ `daf87da6...`, recorded base `816f946c...`; base stale frente a live `43fdf70e...`. Además, su exact-head F0/0.9 run `33454881387` está en FAILURE; old-head green no sustituye diagnosis + refresh/exact-head. WOZ133 posee la única conditional integration lane sobre #89.

**Principio:** no falsear provider, capacity, payments, DNS, deployment, staging, legal compliance ni independent counsel review sin evidencia aplicable.
