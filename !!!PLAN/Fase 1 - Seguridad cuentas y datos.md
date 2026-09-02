# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE153:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

Authorization/tenant controls, temp-auth/capabilities, lifecycle/RO decisions, PostgreSQL durability/migrations y restore/recovery permanecen PASS. D10.1 conserva RPO ~7 min, RTO `3643 s` y off-provider encrypted readback/SHA match. No repetir drills sin invalidación.

## D10.2 — MAP COMPLETE / NOT READY

Blockers de alpha interna 3–5 cuentas se consolidan en 1.7; autorización final = 1.8; ejecución = 1.9.

### PROVEN / estado vivo

- #92, #94, #95 y #96 están integrados en F2/12.1. #98 apareció después de CYCLE152 como candidate exact-base `aa445095...`, head `00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c`; está OPEN y aún no convierte runtime/candidate en canonical integrated evidence.
- Issue #97 está OPEN y explícitamente marcado `Must be addressed before Beta 1`; startup/reveal performance cross-platform pasa a blocker pre-Beta separado, después del cleanup #98 por overlap de superficies.
- Windows Auth #93 conserva exact-green evidence histórica en old baseline; base `134a293...` stale contra `aa445095...`.
- AAA114 revalidó F2/13.2 durable Review gap y paró correctamente por write surface; sigue abierto.
- La decisión D8 de recent reauth existe; falta seam productiva consumible por Settings/Trash. Owner CYCLE153 = BBB148.

### HARD / ACTIVE BLOCKERS para alpha / apertura real de F5

1. **F2/12.1 / PR #98:** candidate funcional productivo nuevo; necesita exact-head Required CI/integration y runtime-source proof. AAA149 = evidence READ-ONLY; WOZ152 = exclusive PR #98 mutation/integration.
2. **Issue #97:** pre-Beta startup/reveal performance; no implementación concurrente con #98 por overlap `src/App.tsx`/startup/platform. Se asigna después del cleanup.
3. **F0/0.9 security P1:** #89 stale-base + F0 audit FAILURE; CYCLE153 queda sin mutation owner, solo fallback READ-ONLY de WOZ152 mientras #98 espera.
4. **F2/13.2 durable Review:** `BLOCKED_WRITE_SURFACE / UNASSIGNED`; factual gap remains.
5. **F1/D8 product seam → F2/15.1:** BBB148 expone seam mínima recent-reauth; después debe volver Trash strong confirmation + durable purge.
6. **F4/25.1 Windows Auth canonicalization:** #93 future refresh/revalidation solo si 1.7 lo mantiene en alpha; global 25.1 conserva otros journeys.

### 1.7 — `[ 🟡 ] REQUEUE AFTER FRESH FACTS`

CYCLE153 procesa AAA148/BBB147/WOZ151 como `NO_RESULT / SUPERSEDED / NOT_PASS`. No se emite 1.7 todavía: primero #98/runtime, luego #97, #89 y recent-reauth deben producir facts suficientemente frescos. Después 1.7 clasifica `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL` antes de 1.8.

### F3 — decisión explícita de aplicabilidad al alpha

- 18.2 provider/payment real scenarios: `UNVERIFIED_EXTERNAL`; excluir si alpha no cobra solo mediante decisión explícita. BBB148 puede inventariar READ-ONLY durante espera externa real de su PRIMARY, sin decidir exclusión.
- 19.2 legal implementation/release backlog: sigue abierto.
- 20.2 runtime160/capacity: no probado; release/scale gate, no representativo de 3–5 cuentas, pero su exclusión del alpha debe quedar explícita.

### Release-only / external tails

Production signing/notarization, hardware matrix amplia, 12–20 testers, public release governance y demás tails continúan `NO-GO`.

## Orden mínimo hacia 1.8

1. procesar #98 con exact-head CI/integration + exact runtime-source evidence;
2. cerrar #97 pre-Beta performance con Web + Desktop evidence;
3. integrar/procesar #89 P1 con exact-head evidence;
4. cerrar seam recent-reauth y luego F2/15.1 o elevar exclusión RO explícita;
5. cerrar F2/13.2 o elevar una exclusión RO explícita sustentada;
6. refresh/revalidar #93 Windows Auth si permanece `IN_ALPHA`;
7. reemitir 1.7 factual classification y registrar aplicabilidad F3 18.2/19.2/20.2.

Solo después corresponde **1.8 — decisión RO final**.
