# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 085:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 software reconciliation integrado; provider/payment scenarios globales siguen abiertos.
- 20.1 software observability integrado; external observability tails siguen abiertos.
- #78 capacity harness integrado; local/synthetic-only no satisface runtime 160.
- #83 durable waitlist permanece OPEN/DRAFT, mergeable, head `803b2143e6ea03f6549118e9241fee320dfccdee`, base exact `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, scope de 3 archivos.
- Exact-head F3 20.2 Durable Waitlist `33388377959` SUCCESS; Desktop Portability/applicable Required-CI family `33388377963` SUCCESS; D6 `33388377952` SUCCESS; D7 `33388377964` SUCCESS.
- `NIGHT-WOZ-083`: no final result at CYCLE 085; superseded; NOT_PASS.
- #76 legal/public routes permanece OPEN/stale/frozen.

## Owner CYCLE 085

**WOZ — `NIGHT-WOZ-084` — F3 / 20.2 / #83.**

PRIMARY: fresh exact recheck; use current authorized GitHub Ready-for-review action; if Ready is verified and base/head/scope/CI remain exact/race-free, merge with expected head `803b2143...` and verify resulting integration SHA/parents. WOZ/#83 is the only integration mutation authorized.

CI-FALLBACK: NONE. Runtime 160 must be measured on the post-#83 integration state if #83 lands.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
Dominio/API/status/support URLs/sender domains, DNS/TLS/redirects/callbacks OAuth y despliegue real siguen requiriendo evidencia productiva. #76 no está integrado.

### 19.2 — `[ 🟡 ] FROZEN`
Privacy/Terms candidate #76 existe, pero falta safe refresh, independent legal review, publication evidence y soporte operativo.

## Día 20

### 20.1 — `[x] SOFTWARE DONE / INTEGRATED`
Structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno integrados por #75. External provider/on-call/status/retention proof no se infiere.

### 20.2 — `[ 🟡 ] HARNESS INTEGRATED / WAITLIST EXACT-HEAD GREEN / RUNTIME CAPACITY UNVERIFIED`
- [x] deterministic parameterized harness #78;
- [x] expected peak aprobado: **80 simultaneous users**;
- [ ] validation **160 simultaneous users (2×)** con runtime aplicable;
- [ ] latency target/result aplicable;
- [ ] error/queue/recovery behavior demostrado;
- [ ] safety margin medida contra 80;
- [ 🟡 ] durable waitlist #83 exact-head CI green but remains Draft/unmerged pending WOZ084 transaction.

Aunque #83 se integre, 20.2 no cierra sin runtime 160 materialmente aplicable. Local/synthetic-only no se convierte en PASS.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
