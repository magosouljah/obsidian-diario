# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE153:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios reales siguen abiertos.
- 19.1 infraestructura pública principal `PROVEN_OWNER_RUNTIME`; external/provider tails aplicables siguen parciales.
- 19.2 #76 reusable pero stale/13+; v1 canónico = **18+**. F0/0.8 review activity `[x]` bajo excepción AI-assisted RO-approved, pero 19.2/backlog legal sustantivo permanece abierto: 12 P0 + 14 P1 + P2/P3 + UNVERIFIED.
- 20.1 software observability integrado; external observability tails abiertos.
- #78 capacity harness integrado; #83 durable waitlist OPEN/DRAFT; runtime160 UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`

Software reconciliation + durable exception queue está probado. 3DS, rejection, late payment, renewal failure, cancel E2E, plan changes, refund, provider webhooks/financial outcomes y full sandbox reconciliation permanecen `UNVERIFIED_EXTERNAL`.

Para una alpha 3–5 cuentas sin cobros, 1.7 debe clasificar explícitamente este gate como `RO_EXCLUDE_CANDIDATE` o `MUST_CLOSE`; no se infiere exclusión automáticamente.

**CYCLE153:** `NIGHT-BBB-148` puede, únicamente si su PRIMARY recent-reauth queda genuinamente esperando CI/build/review externo, usar CI-FALLBACK READ-ONLY para inventariar esta evidencia y clasificarla `SOFTWARE_PROVEN / UNVERIFIED_EXTERNAL / NOT_REPRESENTATIVE_OF_3_5_ACCOUNT_ALPHA`. No ejecuta pagos/provider mutation y no toma la decisión RO de exclusión.

## 19.1 — `[ 🟡 ] PUBLIC SOFTWARE/RUNTIME IMPROVED / EXACT SOURCE BINDING OPEN`

Owner evidence previo mantiene `/web-health`, auth-health, www→apex y TLS probados en evidencia aplicable. #87, #88 y #90 están integrados. PR #98 reporta clean deployment productivo con public/local health PASS, library materialization, artwork y playback funcional; sin embargo #98 sigue OPEN y CYCLE153 exige distinguir runtime exact-source-bound de behavior source-unbound antes de cerrar F2/12.1 o promover 19.1 más allá de lo literal.

## 19.2 — `[ 🟡 ] LEGAL IMPLEMENTATION OPEN / REVIEW TASK COMPLETE`

PR #76 @ `36d218609cf2488997755312fa2dafd0a019d070` permanece stale; 13+ contradice v1 **18+** y Settings copy requiere reconciliación. No repetir hasta cambio material de surface/tooling y owner explícito.

F0/0.8 es `[x]` solo porque RO sustituyó independent-counsel review por AI-assisted audit del `2026-08-31` y aceptó riesgo residual. No es attorney review ni compliance. Sus **12 P0 + 14 P1** siguen release/implementation gates; P2/P3 y `UNVERIFIED` siguen backlog/risk. 1.7 debe clasificar aplicabilidad al alpha sin declararlos resueltos.

## 20.1 — `[x] SOFTWARE DONE / INTEGRATED`

Structured redacted events, counters, routes, kill switches, tests/runbook integrados por #75. External provider/on-call/status/retention proof no se infiere.

## 20.2 — `[ 🟡 ] RUNTIME UNVERIFIED`

#78 harness integrado; expected peak 80. Falta runtime aplicable a **160 concurrent users**, latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin. #83 @ `803b2143...` sigue OPEN/DRAFT y stale. Integrarlo tampoco cerraría runtime160.

Para alpha 3–5 cuentas, 1.7 debe clasificar explícitamente 20.2; no se fabrica como prerequisito representativo ni se excluye sin decisión RO.

## Cross-phase security tail

PR #89 F0/0.9 contiene P1 DNS-rebinding SSRF corrective + audit AI-assisted. CYCLE153 no le asigna mutation owner porque WOZ152 fue movido a PR #98. #89 sigue OPEN @ `daf87da6...`, base `816f946c...` stale y security run `33454881387` FAILURE. Solo puede recibir inventario READ-ONLY como fallback de WOZ152 durante espera externa real de #98.

**Principio:** no falsear provider, capacity, payments, DNS, deployment, staging, legal compliance ni independent counsel review sin evidencia aplicable.
