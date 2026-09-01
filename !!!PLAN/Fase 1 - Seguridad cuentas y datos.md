# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE 104:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[ 🟡 ] NOT_READY_FOR_RO_DECISION`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

D6 authorization/tenant controls, D7 temp-auth/capabilities, D8 lifecycle/RO decisions, D9 PostgreSQL durability/migrations and D10.1 restore/recovery remain PASS. No factual invalidation observed. Canonical evidence remains PRs #43/#44/#46/#49/#52/#53/#56 and Issue #41 gates `5455677550`, `5457172823`, `5460381842`, `5460959369`, `5470149521`. D10.1 retains RPO ~7 min and RTO `3643 s` plus encrypted off-provider readback/SHA match.

**No repetir PITR/restore/cutover/restart/migrations/rotation.**

## D10.2 — `[ 🟡 ] NOT_READY_FOR_RO_DECISION`

`NIGHT-WOZ-102` terminó factual y READ-ONLY; Issue #41 `5486382155`:
- `PROVEN`: D6–D10.1 y línea técnica interna aplicable;
- `BLOCKED_BY_F2`: public Web normal startup sigue `Loading Galer`; 13.2 durable Review abierto; 15.1 recent-reauth/confirmation/deterministic Trash abierto;
- `BLOCKED_BY_F4`: packaged Windows Auth exact #84 `f53d46f...`, run `33449587244` / job `99676242317` = FAILURE;
- `BLOCKED_BY_F3`: provider/payment real scenarios y release/public/runtime-160 tails siguen sin evidencia global;
- `BLOCKED_EXTERNAL`: F0 historical cleanup y release/admin tails, explícitamente no bloqueantes para trabajo interno pero no cerrados para release;
- `RO_DECISION_REQUIRED`: autorización final de alpha interna 3–5 cuentas y decisiones explícitas de aplicabilidad/exclusión de features/gates no esenciales al alpha.

Conjunto mínimo antes de reconsiderar `READY_FOR_RO_DECISION`:
1. resolver F2/12.1 normal Web startup;
2. obtener PASS literal F4/25.1 Windows packaged auth;
3. cerrar o recibir decisión RO explícita de exclusión para F2/13.2 y F2/15.1 dentro del scope de alpha.

**CYCLE 104:** D10.2 queda sin owner material mientras AAA100 y BBB099 atacan sus blockers; WOZ103 se reasigna a F0/#86. No lanzar alpha, crear testers, cobrar, usar credenciales ni mutar provider/infra desde este gate.

**Principio:** readiness de alpha interna ≠ release público; F5 permanece cerrado hasta F0–F4 gates reales.
