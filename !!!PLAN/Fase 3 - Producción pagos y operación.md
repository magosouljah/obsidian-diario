# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 100:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2 software reconciliation integrado; provider/payment scenarios globales siguen abiertos. `NIGHT-WOZ-098` produjo evidence-gap map factual y cerró su lane sin PASS.
- 20.1 software observability integrado; external observability tails siguen abiertos.
- #78 capacity harness integrado; local/synthetic-only no satisface runtime 160.
- #83 durable waitlist permanece OPEN/DRAFT, mergeable, head `803b2143e6ea03f6549118e9241fee320dfccdee`, base exact `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; exact-head F3 20.2 Durable Waitlist `33388377959` SUCCESS y otros gates observados verdes, pero supported Draft→Ready path sigue materialmente bloqueado. No owner de mutación en CYCLE 100.
- Runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin siguen UNVERIFIED aun si #83 integra después.
- 19.1 queda reducido a blockers externos de DNS/TLS/API/status/OAuth/sender/deployment después de WOZ096.
- #76 legal/public routes permanece OPEN/Ready/mergeable pero stale; CYCLE 100 encontró contradicción material de eligibility 13+ en #76 vs requisito canónico v1 18+, además del in-app SettingsPanel legal copy gap reconocido por el propio PR. `NIGHT-WOZ-099` es owner exclusivo de reconciliar ese candidate existente. NO MERGE.

## Día 18

### 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`

`NIGHT-WOZ-098` terminó `BLOCKED_STOP / F3/18.2 EVIDENCE_GAP_MAP_UPDATED` READ-ONLY.

Clasificación reusable:
- reconciliation core + durable exception queue: `PROVEN_SOFTWARE` mediante `cloud-server/billing-reconciliation.js` y `cloud-server/tests/billing-reconciliation.test.cjs`;
- cancel/status vocabulary: `PARTIAL` — estados aceptados no prueban lifecycle/provider/financial outcome;
- 3DS, rechazo, pago tardío, renewal failed real, cancel E2E, upgrade/downgrade, refund, provider webhook real/staging, ledger/financial outcomes, grace-period policy aprobada y 100% expected sandbox reconciliation: `UNVERIFIED_EXTERNAL`.

Issue #41 `5485068226`.

**Owner CYCLE 100:** ninguno para 18.2. Siguiente avance útil requiere Stripe/provider staging autorizado y/o decisión RO; no repetir inspección software para fabricar PASS.

## Día 19

### 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`
Established: candidate #76 names `beatgaler.com`, `/privacy`, `/terms`, `support@beatgaler.com`; esto no prueba deployment/DNS/sender/OAuth.

`NIGHT-WOZ-096` terminó `BLOCKED_STOP / F3/19.1 PUBLIC_SURFACE_EVIDENCE_BOUNDED`:
- no hizo mutaciones;
- bounded public lookup no produjo DNS autoritativo, TLS/certificate ni HTTP status verificable;
- resolver disponible devolvió `Temporary failure in name resolution`, por lo que no se fabricó claim NXDOMAIN;
- provider/deployment/OAuth/sender privados siguen `UNVERIFIED`.

**Owner CYCLE 100:** ninguno para 19.1. No repetir la misma superficie incapaz ni inferir producción desde código/docs.

### 19.2 — `[ 🟡 ] IN PROGRESS / #76 RECONCILIATION`

PR #76 `legal/privacy-terms-v1` @ `36d218609cf2488997755312fa2dafd0a019d070` es material reusable pero no integrable tal cual:
- base histórica `a9d35a3...` vs integración viva `816f946c...`;
- Privacy/Terms permiten 13+/minimum age mientras F0 canonical business decision fija v1 **18+**;
- el PR reconoce que `src/components/SettingsPanel.tsx` conserva copy legal temporal/placeholders/old contact y no está reconciliado con canonical docs;
- `/privacy` y `/terms` existen como candidate intent, pero deployment/SPA fallback no está probado.

**Owner CYCLE 100:** `NIGHT-WOZ-099`.
- REUSE-FIRST sobre #76, no segundo PR;
- reconciliar solo decisiones ya canónicas, incluyendo eligibility 18+, current operator/contact/billing decisions y hidden implementation-provider vocabulary;
- preferir una fuente canónica para in-app/public legal copy;
- history-preserving refresh contra baseline vivo + focused tests/build + exact-head CI;
- NO MERGE;
- independent legal review y production deployment siguen UNVERIFIED.

CI-FALLBACK de WOZ099, únicamente si #76 entra en WAITING_CI: F1/D10.2 decision map READ-ONLY, completamente independiente de #76.

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

**Regla CYCLE 100:** no repetir la misma Ready action, no usar GraphQL workaround/bypass y no asignar runtime-160 como si #83 ya estuviera integrado. Reabrir la transacción #83 solo cuando exista un cambio material verificable en la ruta soportada.

No cerrar 20.2 por CI software ni por harness local/sintético. Integrar #83 tampoco sustituirá runtime 160 aplicable.

**Principio:** no falsear proveedor, capacidad, pagos, DNS, legal review o staging real sin evidencia externa/productiva.
