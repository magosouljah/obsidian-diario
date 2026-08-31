# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 101:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2: reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios globales siguen abiertos.
- 19.1: `PARTIAL / EXTERNAL`; no inferir producción desde código/docs.
- 19.2: #76 es candidate reusable pero stale y contradictorio con eligibility canónica 18+; `NIGHT-WOZ-100` es owner exclusivo de reconciliación, **NO MERGE**.
- 20.1 software observability integrado; external observability tails siguen abiertos.
- #78 capacity harness integrado; no sustituye runtime real.
- #83 durable waitlist sigue OPEN/DRAFT/mergeable @ `803b2143e6ea03f6549118e9241fee320dfccdee`, exact base `816f946c...`; supported Draft→Ready path continúa materialmente bloqueado. PARKED.
- Runtime target aprobado: expected 80 simultaneous users; validation exacta 160. Latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin siguen UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`

`NIGHT-WOZ-098` = `BLOCKED_STOP / EVIDENCE_GAP_MAP_UPDATED`:
- reconciliation core + durable exception queue = `PROVEN_SOFTWARE`;
- cancel/status vocabulary = `PARTIAL`;
- 3DS, rejection, late payment, renewal failure, cancel E2E, upgrade/downgrade, refund, provider webhooks, financial outcomes y full sandbox reconciliation = `UNVERIFIED_EXTERNAL`.

Owner-approved billing policy exists en Issue #41 (grace 3 días, fallback Free/no deletion, cancel period-end, upgrade immediate after confirmed payment, downgrade next cycle, refund rules). Eso es decisión RO, no provider/runtime PASS.

## 19.1 — `[ 🟡 ] PARTIAL / EXTERNAL`

Canonical domain/contact intent: `beatgaler.com`, `support@beatgaler.com`, OAuth callback values ya decididos. Issue #41 contiene evidencia previa de `api.beatgaler.com` TLS/Let's Encrypt, pero DNS/TLS/HTTP/status/support/mail/OAuth/deployment completo actual no queda demostrado por la superficie conectada usada en WOZ096. No repetir un lookup incapaz ni degradar evidencia previa.

## 19.2 — `[ 🟡 ] IN PROGRESS / #76 RECONCILIATION`

PR #76 `legal/privacy-terms-v1 @ 36d218609cf2488997755312fa2dafd0a019d070`:
- OPEN/Ready/mergeable;
- base stale `a9d35a3...` vs live `816f946c...`;
- Privacy/Terms dicen 13+/minimum age, contradiciendo v1 canónico **18+**;
- PR body reconoce SettingsPanel legal copy/placeholders viejos;
- `/privacy` y `/terms` route intent existe, deployment/SPA fallback no probado.

**Owner CYCLE 101: `NIGHT-WOZ-100`.** Reuse #76; reconciliar 18+, decisiones legales/business ya aprobadas y una fuente canónica para Settings/public; history-preserving refresh + focused tests/build + exact-head CI; **NO MERGE**. External legal review/public deployment permanecen UNVERIFIED.

CI-FALLBACK solo si PRIMARY entra realmente en WAITING_CI: F1/D10.2 alpha-readiness decision map READ-ONLY. D10.1 ya está PASS.

## 20.1 — `[x] SOFTWARE DONE / INTEGRATED`

Structured redacted events, bounded counters, condition→route mapping, kill switches, tests/runbook internos integrados por #75. External provider/on-call/status/retention proof no se infiere.

## 20.2 — `[ 🟡 ] HARNESS INTEGRATED / WAITLIST GREEN / TOOLING-BLOCKED / RUNTIME UNVERIFIED`

- [x] deterministic parameterized harness #78;
- [x] expected peak = **80 simultaneous users**;
- [ ] validation **160 simultaneous users (2×)** en runtime aplicable;
- [ ] latency/error/queue/recovery result aplicable;
- [ ] safety margin medida;
- [ 🟡 ] #83 exact-head green pero OPEN/DRAFT/unmerged.

No repetir Draft→Ready con el mismo connector failure; reabrir solo con cambio material verificable en supported tooling. Integrar #83 tampoco cerraría runtime 160.

**Principio:** no falsear provider, capacity, payments, DNS, legal review o staging sin evidencia externa/productiva.
