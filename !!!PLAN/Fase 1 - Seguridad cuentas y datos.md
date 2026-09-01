# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE143:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

Authorization/tenant controls, temp-auth/capabilities, lifecycle/RO decisions, PostgreSQL durability/migrations y restore/recovery permanecen PASS. D10.1 conserva RPO ~7 min, RTO `3643 s` y off-provider encrypted readback/SHA match. No repetir drills sin invalidación.

## D10.2 — MAP COMPLETE / NOT READY

Blockers de alpha interna 3–5 cuentas se consolidan en 1.7; autorización final = 1.8; ejecución = 1.9.

### PROVEN / estado vivo

- #92, #94, #95 y #96 están integrados en F2/12.1. PR #96 final head `6247173ead703f831801fa103ca465fea04e5793`, base `43fdf70e...`, merge `aa445095...`; Required CI exact-head SUCCESS. Esto es software evidence, no public runtime proof.
- Windows Auth #93 conserva exact-green evidence histórica en old baseline; su base `134a293...` stale contra `aa445095...` no cuenta como canonical integration evidence.
- AAA114 revalidó F2/13.2 durable Review gap y paró correctamente por write surface; sigue abierto.
- La decisión D8 de recent reauth existe, pero falta seam productiva consumible por Settings/Trash; owner BBB138.

### HARD / ACTIVE BLOCKERS para alpha

1. **F2/12.1:** software lineage integrada; public runtime proof exacto post-`aa445095...` sigue pendiente. Owner AAA139 READ-ONLY para evidencia/clasificación.
2. **F0/0.9 security P1:** #89 stale-base + current F0 audit FAILURE; owner WOZ142 para diagnosis/refresh/revalidation/integration.
3. **F2/13.2 durable Review:** `BLOCKED_WRITE_SURFACE / UNASSIGNED`; factual gap remains.
4. **F1/D8 product seam → F2/15.1:** owner BBB138 expone seam mínima recent-reauth; después debe volver Trash strong confirmation + durable purge.
5. **F4/25.1 Windows Auth canonicalization:** #93 requiere future refresh/revalidation si sigue IN_ALPHA; global 25.1 además conserva otros journeys.

### 1.7 — `[ 🟡 ] REQUEUE AFTER FRESH FACTS`

`NIGHT-AAA-138`, `NIGHT-BBB-137` y `NIGHT-WOZ-141` no produjeron RESULTADO DEL TURNO verificable. JOBS CYCLE143 recalculó desde cero y mantiene primero los tres reducers factuales/productivos de mayor impacto: 12.1 runtime, #89 y recent-reauth. Después se reemitirá 1.7 para clasificación `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL` antes de 1.8.

### F3 — decisión explícita de aplicabilidad al alpha

- 18.2 provider/payment real scenarios: `UNVERIFIED_EXTERNAL`; excluir si alpha no cobra solo mediante decisión explícita.
- 19.2 legal implementation/release backlog: sigue abierto.
- 20.2 runtime160/capacity: no probado; release/scale gate, no representativo de 3–5 cuentas, pero su exclusión del alpha debe quedar explícita.

### Release-only / external tails

Production signing/notarization, hardware matrix amplia, 12–20 testers, public release governance y demás tails continúan `NO-GO`.

## Orden mínimo hacia 1.8

1. cerrar/reducir 12.1 public runtime proof con evidencia exacta;
2. integrar/procesar #89 P1 con exact-head evidence;
3. cerrar seam recent-reauth y luego F2/15.1 o elevar exclusión RO explícita;
4. cerrar F2/13.2 o elevar una exclusión RO explícita sustentada;
5. refresh/revalidar #93 Windows Auth evidence si permanece `IN_ALPHA`;
6. reemitir 1.7 factual classification con facts frescos y registrar aplicabilidad F3 18.2/19.2/20.2.

Solo después corresponde **1.8 — decisión RO final**.
