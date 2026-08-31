# Fase 3 — Producción, pagos, legal y operación

> GitHub/runtime vivo prevalece. Leer `Plan Maestro.md` antes de actuar.

**Baseline vivo CYCLE 103:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado compacto

- 17.1 / 17.2 / 18.1 `[x]`.
- 18.2: reconciliation core/exception queue `PROVEN_SOFTWARE`; provider/payment scenarios globales siguen abiertos.
- 19.1: infraestructura pública principal ahora `PROVEN_OWNER_RUNTIME`; legal/public-route/support/OAuth tails siguen parciales. El nuevo `Loading Galer` es bug funcional F2, no fallo de deploy.
- 19.2: #76 reusable pero stale/13+ y bloqueado por falta de refresh history-preserving; sin owner CYCLE 103.
- 20.1 software observability integrado; external observability tails abiertos.
- #78 capacity harness integrado; no sustituye runtime real.
- #83 durable waitlist sigue OPEN/DRAFT @ `803b2143e6ea03f6549118e9241fee320dfccdee`, exact base `816f946c...`; Ready tooling blocker permanece. Runtime 160 UNVERIFIED.

## 18.2 — `[ 🟡 ] GLOBAL PROVIDER/PAYMENT EVIDENCE OPEN`

`NIGHT-WOZ-098` = `BLOCKED_STOP / EVIDENCE_GAP_MAP_UPDATED`:
- reconciliation core + durable exception queue = `PROVEN_SOFTWARE`;
- cancel/status vocabulary = `PARTIAL`;
- 3DS, rejection, late payment, renewal failure, cancel E2E, upgrade/downgrade, refund, provider webhooks, financial outcomes y full sandbox reconciliation = `UNVERIFIED_EXTERNAL`.

Owner-approved billing policy exists en Issue #41; eso es decisión RO, no provider/runtime PASS.

## 19.1 — `[ 🟡 ] PUBLIC INFRA PROVEN / FUNCTIONAL + EXTERNAL TAILS OPEN`

Canonical domain/contact intent: `beatgaler.com`, `support@beatgaler.com`.

**Owner runtime evidence — Issue #41 `5485984669`:**
- `https://beatgaler.com/web-health` => `ok`;
- `https://beatgaler.com/beatgaler-api/auth/health` => backend reachable con `account_auth:true`;
- `https://www.beatgaler.com` => 301 a apex;
- TLS `beatgaler.com` + `www.beatgaler.com` reissued vía Certbot; auto-renew scheduled.

Por instrucción owner, la infraestructura pública/deploy **no se reabre** por el síntoma funcional posterior. Abrir el apex queda detenido en `Loading Galer`; eso se rastrea en F2/12.1 bajo AAA099.

PR #85 `fix(web): make production deploy script PowerShell-safe` sigue OPEN/Ready, owner-owned, exact base live; head vivo verificado `ab25e89570de66189612c7a4677161a73bbe5d5d`. AAA/BBB/WOZ no lo mutan ni duplican. Su existencia tampoco es requisito para negar la evidencia runtime ya observada del deploy actual.

Permanecen sin cierre global 19.1 donde aplique: direct `/privacy`/`/terms` + SPA fallback, support/mail/OAuth public-surface evidence y demás tails externos. No inferirlos desde health/TLS.

## 19.2 — `[ 🟡 ] BLOCKED ON REFRESH-CAPABLE EXECUTION SURFACE`

PR #76 `legal/privacy-terms-v1 @ 36d218609cf2488997755312fa2dafd0a019d070` sigue OPEN/Ready pero base stale; Privacy/Terms 13+ contradice v1 canónico **18+** y Settings legal copy requiere reconciliación.

`NIGHT-WOZ-100` confirmó REUSE-FIRST y terminó `BLOCKED_STOP / PREFLIGHT_COMPLETE / NO_MUTATION` (Issue #41 `5485787222`): la superficie soportada no permite el history-preserving branch refresh requerido. No repetir la misma operación incapaz.

**Siguiente requisito:** superficie con refresh history-preserving; luego reconciliar 18+, decisiones legales aprobadas y fuente canónica Settings/public; focused tests/build + exact-head CI. **NO MERGE hasta nueva autorización.**

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

**Principio:** no falsear provider, capacity, payments, DNS, legal review, deployment o staging sin evidencia externa/productiva.
