# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 095:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 software reconciliation integrado; provider/payment scenarios globales siguen abiertos.
- 20.1 software observability integrado; external observability tails siguen abiertos.
- #78 capacity harness integrado; local/synthetic-only no satisface runtime 160.
- #83 durable waitlist permanece OPEN/DRAFT, mergeable, head `803b2143e6ea03f6549118e9241fee320dfccdee`, base exact `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, scope exacto de 3 archivos.
- Exact-head F3 20.2 Durable Waitlist `33388377959` SUCCESS; Desktop Portability `33388377963` SUCCESS; D6 `33388377952` SUCCESS; D7 `33388377964` SUCCESS.
- `NIGHT-WOZ-092` ejecutó una sola vez la acción soportada `mark_pull_request_ready_for_review`; falló dentro del conector con `GithubGraphQLAPIError` porque `Repository.fullDatabaseId` es undefined. Postcheck inmediato: #83 siguió OPEN/DRAFT, mismo head/base/scope, merged=false. Issue #41 `5482892475`.
- No se verificó cambio material del path soportado desde ese blocker. #83 queda `PARKED / TOOLING_BLOCKED` en CYCLE 095 y no tiene owner de mutación.
- Runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin siguen UNVERIFIED aun si #83 integra después.
- 19.1 sigue reducido a blockers externos de DNS/TLS/API/status/OAuth/sender/deployment.
- #76 legal/public routes permanece OPEN/stale/frozen.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
Established: candidate #76 names `beatgaler.com`, `/privacy`, `/terms`, `support@beatgaler.com`; esto no prueba deployment/DNS/sender/OAuth.

`NIGHT-WOZ-094` puede usar **CI-FALLBACK** solo durante una espera real de CI de su PRIMARY F2/15.1 para recolectar evidencia pública READ-ONLY: resolución DNS/TLS, hostnames/endpoints públicamente observables y status/support/security-abuse visibles. Debe marcar `UNVERIFIED` cualquier hecho que requiera consola/provider credentials, sender verification privada, OAuth config privada o cambios de infraestructura. STOP antes de cualquier mutación o edición legal/#76.

### 19.2 — `[ 🟡 ] FROZEN`
#76 existe, pero falta safe refresh, independent legal review, publication evidence y soporte operativo.

## Día 20

### 20.1 — `[x] SOFTWARE DONE / INTEGRATED`
Structured redacted events, bounded counters, condition→route mapping, kill switches, tests y runbook interno integrados por #75. External provider/on-call/status/retention proof no se infiere.

### 20.2 — `[ 🟡 ] HARNESS INTEGRATED / WAITLIST EXACT-HEAD GREEN / TOOLING-BLOCKED / RUNTIME UNVERIFIED`
- [x] deterministic parameterized harness #78;
- [x] expected peak aprobado: **80 simultaneous users**;
- [ ] validation **160 simultaneous users (2×)** con runtime aplicable;
- [ ] latency target/result aplicable;
- [ ] error/queue/recovery behavior demostrado;
- [ ] safety margin medida contra 80;
- [ 🟡 ] durable waitlist #83 exact-head CI green, todavía OPEN/DRAFT/unmerged; supported Draft→Ready path failed before mutation in WOZ092.

**Regla CYCLE 095:** no repetir la misma Ready action, no usar GraphQL workaround/bypass y no asignar runtime-160 como si #83 ya estuviera integrado. Reabrir la transacción #83 solo cuando exista un cambio material verificable en la ruta soportada.

No cerrar 20.2 por CI software ni por un harness local/sintético. Integrar #83 tampoco sustituirá runtime 160 aplicable.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
