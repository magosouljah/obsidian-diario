# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo del mapa D10.2:** `integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

Authorization/tenant controls, temp-auth/capabilities, lifecycle/RO decisions, PostgreSQL durability/migrations y restore/recovery permanecen PASS. No factual invalidation observada. D10.1 conserva RPO ~7 min, RTO `3643 s` y off-provider encrypted readback/SHA match. **No repetir PITR/restore/cutover/restart/migrations/rotation.**

## D10.2 — `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`

D10.2 es el **mapa de readiness** para una alpha interna acotada de 3–5 cuentas. Que el mapa encuentre blockers no mantiene abierto el trabajo de mapear: esos blockers pasan a **1.7**. La autorización final sigue separada en **1.8** y la ejecución en **1.9**.

### PROVEN

- D6–D10.1 y la línea técnica interna aplicable permanecen cerrados.
- Infraestructura Web pública básica ya tiene evidencia de health/TLS; eso no sustituye el startup funcional normal.
- El merge #88 a `1dbf60e...` cerró únicamente el seam técnico/preparatorio Authenticode/RFC3161; no equivale a production signing ni resuelve Windows packaged auth.

### HARD BLOCKERS para candidato de alpha

1. **F2/12.1 — Web startup:** el flujo normal público sigue sin evidencia nueva de salir de `Loading Galer`. Debe terminar determinísticamente o fallar con estado recuperable; no puede quedar colgado.
2. **F4/25.1 — Windows packaged auth:** #84 @ `f53d46f...` conserva old-head generic CI verde, pero el journey literal `33449587244` = **FAILURE**. Se requiere PASS literal en lineage refrescada/exact-head.
3. **F0/0.9 — security P1 paralelo:** #89 contiene el corrective DNS-rebinding/SSRF pero sigue sin integración vigente al snapshot. Un P1 de seguridad conocido no debe quedar silenciosamente abierto al autorizar la alpha. Este punto se resuelve fuera del scope F2/F3/F4 de 1.7, pero se revalida en 1.8.

### CLOSE OR RO-EXCLUDE antes de 1.8

- **F2/13.2 — durable Review Save/Save All:** existe gap probado de completion/no-silent-loss. Si Review forma parte de la alpha, debe cerrarse; si no, RO debe excluirlo explícitamente del scope de la alpha.
- **F2/15.1 — Empty Trash:** faltan recent-reauth, strong confirmation y boundary durable/determinístico. Debe cerrarse o quedar explícitamente fuera del scope de alpha.

### F3 — decisión explícita de aplicabilidad al alpha

Para una alpha invite-only de 3–5 cuentas sin billing público, estos gates no se pueden marcar PASS por inferencia, pero tampoco deben bloquear automáticamente si RO los excluye explícitamente del alcance:

- **18.2 provider/payment real scenarios** — mantener `UNVERIFIED_EXTERNAL`; excluir del alpha si no hay cobros ni exposición a billing.
- **19.2 legal implementation/release backlog** — permanece abierto para release; RO debe decidir qué superficies legales son obligatorias para las cuentas internas concretas antes de 1.8.
- **20.2 runtime160/capacity** — sigue sin prueba real de 160 concurrentes; no es representativo de 3–5 cuentas, pero permanece gate de release/scale y no se marca PASS.

### Release-only / external tails

Production Authenticode/notarization, hardware matrix amplia, 12–20 testers, public release governance y demás tails de publicación continúan `NO-GO`. **No se usan para fingir que la alpha está lista, pero tampoco se exige cerrarlos para completar este mapa.** Su aplicabilidad final a la alpha se confirma en 1.8.

## Salida D10.2 → 1.7

**D10.2 queda cerrado como mapa.** El estado de readiness resultante es `NOT_READY`.

Orden mínimo de 1.7:
1. resolver F2/12.1 normal Web startup;
2. obtener PASS literal F4/25.1 Windows packaged auth;
3. cerrar o preparar decisión RO explícita de exclusión para F2/13.2;
4. cerrar o preparar decisión RO explícita de exclusión para F2/15.1;
5. revalidar #89/F0 security P1 y clasificar F3 18.2/19.2/20.2 como `IN_ALPHA` o `EXCLUDED_FROM_ALPHA` sin alterar sus gates de release.

Solo después de esa revalidación corresponde **1.8 — decisión RO final**. No crear testers, cobrar, mutar provider/infra ni ejecutar la alpha desde D10.2.
