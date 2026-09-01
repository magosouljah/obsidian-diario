# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE 109:** `integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[ 🟡 ] NOT_READY_FOR_RO_DECISION`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

Authorization/tenant controls, temp-auth/capabilities, lifecycle/RO decisions, PostgreSQL durability/migrations y restore/recovery permanecen PASS. No factual invalidation observada. D10.1 conserva RPO ~7 min, RTO `3643 s` y off-provider encrypted readback/SHA match. **No repetir PITR/restore/cutover/restart/migrations/rotation.**

## D10.2 — `[ 🟡 ] NOT_READY_FOR_RO_DECISION`

Mapa factual CYCLE 109:
- `PROVEN`: D6–D10.1 y línea técnica interna aplicable;
- `BLOCKED_BY_F2`: normal Web startup sigue sin PASS de salida de `Loading Galer`; 13.2 durable Review abierto; 15.1 recent-reauth/confirmation/deterministic Trash abierto;
- `BLOCKED_BY_F4`: #84 @ `f53d46f...` stale; generic old-head CI SUCCESS pero literal Windows Auth `33449587244` = FAILURE;
- `BLOCKED_BY_F3/F0`: provider/payment real scenarios y release/admin/signing/capacity/legal implementation tails siguen;
- `RO_DECISION_REQUIRED`: autorización final de alpha interna y decisiones explícitas de aplicabilidad/exclusión de features/gates no esenciales al alpha.

El merge #88 a `1dbf60e...` cierra únicamente el seam técnico/preparatorio Authenticode/RFC3161; no resuelve D10.2 ni production signing.

Conjunto mínimo antes de reconsiderar `READY_FOR_RO_DECISION`:
1. resolver F2/12.1 normal Web startup;
2. obtener PASS literal F4/25.1 Windows packaged auth;
3. cerrar o recibir decisión RO explícita de exclusión para F2/13.2 y F2/15.1 dentro del scope de alpha.

**CYCLE 109:** AAA105 ataca F2/12.1; BBB104 ataca F4/25.1; WOZ108 trabaja #89 sin sustituir estos blockers. F5 permanece cerrado.
