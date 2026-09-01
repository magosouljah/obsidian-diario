# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE120:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

Authorization/tenant controls, temp-auth/capabilities, lifecycle/RO decisions, PostgreSQL durability/migrations y restore/recovery permanecen PASS. D10.1 conserva RPO ~7 min, RTO `3643 s` y off-provider encrypted readback/SHA match. No repetir drills sin invalidación.

## D10.2 — MAP COMPLETE / NOT READY

Blockers de alpha interna 3–5 cuentas se consolidan en 1.7; autorización final = 1.8; ejecución = 1.9.

### PROVEN / estado vivo

- #92, #94 y #95 están integrados en F2/12.1; #95 corrige el bound temporary Web session id, pero falta public runtime proof post-#95.
- Windows Auth #93 conserva exact-green evidence histórica en old baseline. GitHub CYCLE120 reporta `mergeable=true`, pero `base_sha=134a293...` sigue stale contra `43fdf70e...`; no cuenta como canonical integration evidence.
- AAA114 revalidó el F2/13.2 durable Review gap, pero STOP correcto por write surface: no branch/PR/tests/CI; 13.2 sigue abierto.
- La decisión D8 de recent reauth existe, pero sigue faltando una seam productiva consumible por Settings/Trash; owner BBB115.

### HARD / ACTIVE BLOCKERS para alpha

1. **F2/12.1 runtime post-#95:** deployment exacto + signed-out/authenticated worker/library + cold/warm evidence.
2. **F0/0.9 security P1:** #89 `mergeable=true` pero base `816f...` stale; owner WOZ119 para refresh/revalidation/integration.
3. **F2/13.2 durable Review:** `BLOCKED_WRITE_SURFACE / UNASSIGNED` CYCLE120; factual gap remains.
4. **F1/D8 product seam → F2/15.1:** owner BBB115 expone seam mínima recent-reauth; después debe volver Trash strong confirmation + durable purge.
5. **F4/25.1 Windows Auth canonicalization:** #93 requiere future refresh/revalidation contra live baseline; global 25.1 además conserva otros journeys.

### 1.7 — `[ 🟡 ] OWNER AAA116 / READ-ONLY CLASSIFICATION`

AAA116 debe clasificar cada blocker material como `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL` con evidencia concreta. Debe cubrir explícitamente F3 18.2/19.2/20.2, F2/12.1, #89, Review, recent-reauth→Trash, #93/25.1 y release-only externals. Esta clasificación no toma decisiones RO, no excluye nada por sí sola y no promueve 1.8.

### F3 — decisión explícita de aplicabilidad al alpha

- 18.2 provider/payment real scenarios: `UNVERIFIED_EXTERNAL`; excluir si alpha no cobra solo mediante decisión explícita.
- 19.2 legal implementation/release backlog: sigue abierto.
- 20.2 runtime160/capacity: no probado; release/scale gate, no representativo de 3–5 cuentas, pero su exclusión del alpha debe quedar explícita.

### Release-only / external tails

Production signing/notarization, hardware matrix amplia, 12–20 testers, public release governance y demás tails continúan `NO-GO`.

## Orden mínimo hacia 1.8

1. completar 1.7 factual classification sin rebajar gates;
2. obtener public runtime proof post-#95 o dejar blocker owner/runtime exacto;
3. integrar/procesar #89 P1 con exact-head evidence;
4. cerrar F2/13.2 o elevar una exclusión RO explícita sustentada;
5. exponer seam recent-reauth y luego cerrar F2/15.1 o elevar exclusión RO explícita;
6. refresh/revalidar #93 Windows Auth evidence si permanece `IN_ALPHA`;
7. registrar explícitamente aplicabilidad F3 18.2/19.2/20.2.

Solo después corresponde **1.8 — decisión RO final**.
