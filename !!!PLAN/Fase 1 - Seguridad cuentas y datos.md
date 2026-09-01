# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo del mapa D10.2 / CYCLE 110:** `integration-v0.8.0-alpha.1 @ 78dd55b72142e69ea32ba6c1ba6d43e246ac6843` al preflight JOBS.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

Authorization/tenant controls, temp-auth/capabilities, lifecycle/RO decisions, PostgreSQL durability/migrations y restore/recovery permanecen PASS. No factual invalidation observada. D10.1 conserva RPO ~7 min, RTO `3643 s` y off-provider encrypted readback/SHA match. **No repetir PITR/restore/cutover/restart/migrations/rotation.**

## D10.2 — `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`

D10.2 es el **mapa de readiness** para una alpha interna acotada de 3–5 cuentas. Que el mapa encuentre blockers no mantiene abierto el trabajo de mapear: esos blockers pasan a **1.7**. La autorización final sigue separada en **1.8** y la ejecución en **1.9**.

### PROVEN

- D6–D10.1 y la línea técnica interna aplicable permanecen cerrados.
- Infraestructura Web pública básica ya tiene evidencia de health/TLS; eso no sustituye startup funcional normal.
- #88 cerró únicamente el seam técnico/preparatorio Authenticode/RFC3161; no equivale a production signing ni resuelve Windows packaged auth.
- #90 software/readiness de OAuth secret rotation está integrado; actual credential rotation/deploy/E2E/revoke sigue externo y NOT DONE.

### HARD BLOCKERS para candidato de alpha

1. **F2/12.1 — Web startup:** AAA105 produjo PR #91 @ `35d44a0dd5ee380f802b3a80b139ca1ca741d5f9`, exact base `78dd55b...`, con corrective bounded para el Worker silencioso. Estado = `CODE_FIX_PROVEN / NO_MERGE / PUBLIC_RUNTIME_PENDING`. Sigue blocker hasta integración + runtime público autenticado del artefacto con el fix.
2. **F4/25.1 — Windows packaged auth:** #84 @ `f53d46f...` conserva old-head generic CI verde, pero journey literal `33449587244` = **FAILURE**. Se requiere PASS literal en lineage refrescada/exact-head.
3. **F0/0.9 — security P1 paralelo:** #89 contiene corrective DNS-rebinding/SSRF pero sigue stale/no integrado al snapshot. Un P1 conocido no debe quedar silenciosamente abierto al autorizar alpha.

### CLOSE OR RO-EXCLUDE antes de 1.8

- **F2/13.2 — durable Review Save/Save All:** gap probado de completion/no-silent-loss. Si Review forma parte de alpha, debe cerrarse; si no, RO debe excluirlo explícitamente.
- **F2/15.1 — Empty Trash:** faltan recent-reauth, strong confirmation y durable deterministic action boundary. Debe cerrarse o quedar explícitamente fuera de alpha.

### F3 — decisión explícita de aplicabilidad al alpha

Para alpha invite-only de 3–5 cuentas sin billing público, estos gates no se marcan PASS por inferencia, pero pueden excluirse del alpha solo por decisión RO explícita:

- **18.2 provider/payment real scenarios** — mantener `UNVERIFIED_EXTERNAL`; excluir del alpha si no hay cobros/billing expuesto.
- **19.2 legal implementation/release backlog** — abierto para release; decidir qué superficies son obligatorias para las cuentas internas concretas.
- **20.2 runtime160/capacity** — no probado; no representativo de 3–5 cuentas, pero sigue gate de release/scale.

### Release-only / external tails

Production Authenticode/notarization, hardware matrix amplia, 12–20 testers, public release governance y demás tails continúan `NO-GO`. No se usan para fingir que alpha está lista ni se exigen para considerar D10.2 map complete.

## Salida D10.2 → 1.7

**D10.2 queda cerrado como mapa. Estado resultante: `NOT_READY`.**

Orden mínimo de 1.7:
1. resolver F2/12.1 integración + runtime normal Web;
2. obtener PASS literal F4/25.1 Windows packaged auth;
3. cerrar o preparar decisión RO explícita de exclusión para F2/13.2;
4. cerrar o preparar decisión RO explícita de exclusión para F2/15.1;
5. revalidar #89/F0 security P1 y clasificar F3 18.2/19.2/20.2 como `IN_ALPHA` o `EXCLUDED_FROM_ALPHA` sin alterar sus gates de release.

Solo después corresponde **1.8 — decisión RO final**. No crear testers, cobrar, mutar provider/infra ni ejecutar alpha desde D10.2.
