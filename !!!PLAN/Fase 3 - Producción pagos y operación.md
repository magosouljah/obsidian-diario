# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 081:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 software reconciliation integrado; provider/payment scenarios globales siguen abiertos.
- 20.1 software observability integrado; external observability tails siguen abiertos.
- #78 capacity harness integrado; máximo histórico `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- #83 durable waitlist sigue OPEN/DRAFT, head `52b58f56d66430db1ecdce9f572680c61d5d9fe3`, 3-file bounded scope, pero su base `957f97771b7a15554cf6e002fe9eb215c71a65cc` quedó stale después del merge #79 a `816f946c...`.
- #76 legal/public routes permanece OPEN/stale/frozen.

## Owner CYCLE 081

**WOZ — `NIGHT-WOZ-080` — F3 / 20.2 / #83.**

PRIMARY: REUSE #83; history-preserving reconciliation sobre live `816f946c...`, fresh focused tests + exact-head CI, vía Draft→Ready autorizada y, solo si base/head/scope/CI/race permanecen exactos, expected-head merge + verify SHA/parents. WOZ/#83 es la única integración mutation autorizada del ciclo.

CI-FALLBACK: durante genuine `WAITING_CI`/external wait de PRIMARY, REUSE #78 READ-ONLY para runtime target 80 expected / 160 validation; medir latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin. Sin code/infra/provider mutation. Recheck PRIMARY al terminar la espera.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
Dominio/API/status/support URLs/sender domains, DNS/TLS/redirects/callbacks OAuth y despliegue real siguen requiriendo evidencia productiva. #76 no está integrado.

### 19.2 — `[ 🟡 ] FROZEN`
Privacy/Terms candidate #76 existe, pero falta safe refresh, independent legal review, publication evidence y soporte operativo.

## Día 20

### 20.1 — `[x] SOFTWARE DONE / INTEGRATED`
Structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno integrados por #75. External provider/on-call/status/retention proof no se infiere.

### 20.2 — `[ 🟡 ] HARNESS INTEGRATED / WAITLIST STALE CANDIDATE / RUNTIME CAPACITY UNVERIFIED`
- [x] deterministic parameterized harness #78;
- [x] expected peak aprobado: **80 simultaneous users**;
- [ ] validation **160 simultaneous users (2×)** con runtime aplicable;
- [ ] latency target/result aplicable;
- [ ] error/queue/recovery behavior demostrado;
- [ ] safety margin medida contra 80;
- [ 🟡 ] durable waitlist #83 requiere reconciliation + fresh exact-head CI + Ready + integration.

Incluso si #83 se integra, 20.2 no cierra sin runtime 160 materialmente aplicable. Local/synthetic-only no se convierte en PASS si el plan no lo acepta.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
