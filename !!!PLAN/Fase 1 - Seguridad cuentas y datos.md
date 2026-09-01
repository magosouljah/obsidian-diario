# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE 108:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[ 🟡 ] NOT_READY_FOR_RO_DECISION`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

D6 authorization/tenant controls, D7 temp-auth/capabilities, D8 lifecycle/RO decisions, D9 PostgreSQL durability/migrations and D10.1 restore/recovery remain PASS. No factual invalidation observed. Canonical evidence remains PRs #43/#44/#46/#49/#52/#53/#56 and Issue #41 gates `5455677550`, `5457172823`, `5460381842`, `5460959369`, `5470149521`. D10.1 retains RPO ~7 min and RTO `3643 s` plus encrypted off-provider readback/SHA match.

**No repetir PITR/restore/cutover/restart/migrations/rotation.**

## D10.2 — `[ 🟡 ] NOT_READY_FOR_RO_DECISION`

Mapa factual vigente:
- `PROVEN`: D6–D10.1 y línea técnica interna aplicable;
- `BLOCKED_BY_F2`: public Web normal startup sigue `Loading Galer`; 13.2 durable Review abierto; 15.1 recent-reauth/confirmation/deterministic Trash abierto;
- `BLOCKED_BY_F4`: packaged Windows Auth #84 @ `f53d46f...`; old-head Required CI SUCCESS pero journey literal `33449587244` / job `99676242317` = FAILURE;
- `BLOCKED_BY_F3/F0`: provider/payment real scenarios, release/admin/signing/runtime tails siguen sin evidencia global;
- `RO_DECISION_REQUIRED`: autorización final de alpha interna 3–5 cuentas y decisiones explícitas de aplicabilidad/exclusión de features/gates no esenciales al alpha.

Los merges #86 y #87 mejoran governance/provenance y public security/status software, pero no resuelven los blockers mínimos de D10.2.

Conjunto mínimo antes de reconsiderar `READY_FOR_RO_DECISION`:
1. resolver F2/12.1 normal Web startup;
2. obtener PASS literal F4/25.1 Windows packaged auth;
3. cerrar o recibir decisión RO explícita de exclusión para F2/13.2 y F2/15.1 dentro del scope de alpha.

**CYCLE 108:** AAA104 ataca F2/12.1; BBB103 ataca F4/25.1; WOZ107 trabaja el P1 software #89 sin sustituir estos blockers. D10.2 no tiene owner material independiente. No lanzar alpha, crear testers, cobrar, usar credenciales ni mutar provider/infra desde este gate.

**Principio:** readiness de alpha interna ≠ release público; F5 permanece cerrado hasta F0–F4 gates reales.
