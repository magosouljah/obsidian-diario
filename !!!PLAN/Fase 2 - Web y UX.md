# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE157:** `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] #92/#94/#95/#96/#98/#99 INTEGRATED / CLEAN CANONICAL PRODUCTION DEPLOYMENT PROOF OPEN`

- #99 `bind Web runtime to exact source SHA` está MERGED; source-binding mechanism integrado en `c2766fb...` y exact-head Required CI fue SUCCESS.
- Exit condition exige clean production deployment desde canonical integration HEAD donde el public marker sea exactamente el integrated SHA.
- CYCLE157 no obtuvo evidencia literal nueva de esa ejecución/readback. **12.1 sigue NOT_PASS**. No se infiere deployment por merge/CI.

### Issue #97 / PR #100 — `[ 🟡 ] PRE-BETA BLOCKER / ACTIVE OWNER WOZ156`

Issue #97 sigue OPEN y `Must be addressed before Beta 1`.

Durante CYCLE157 apareció PR #100 `F2/97: instrument startup and library reveal surfaces`, OPEN/Ready, exact base `c2766fb...`, head `5f0a0727edacbcb404eb4e31571468262744ec95`. El delta es observational instrumentation: timeline Web/Desktop, visible startup-surface taxonomy y beat-card counts. Su propio scope declara que no cambia startup UX, routing, library truth ni performance behavior. CI exact-head está en curso.

`NIGHT-WOZ-156` posee #97/#100 exclusivamente: REUSE #100, obtener measurements Web+Desktop, aislar causal bottleneck y convertir esa misma lineage en la correction mínima shared/cross-platform; instrumentation-only no puede marcar #97 PASS ni integrarse como si fuera cierre. Conditional merge #100 only después de actual correction + exact applicable evidence/CI + race-free expected-head.

### 13.1 — `[ 🟡 ] FROZEN`

#69 Web y #70 Server siguen candidates históricos stale/frozen; solo REUSE bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP / BLOCKED_WRITE_SURFACE`

AAA114 probó que Review puede avanzar/cerrar antes de durable cloud completion. `platform.cloudData.commitImportedBeat()` aporta boundary awaitable/retry-safe y #69 conserva semantics reutilizables. CYCLE157 sigue `UNASSIGNED`; no abrir concurrentemente mientras #97/#100 ocupe App/startup/shared surfaces.

### 14.1 / 14.2

#98 prueba funcionalidad Web reportada de playback/artwork; performance/queue/browser evidence no se promueve más allá de lo literal. #97 concentra startup/reveal pre-Beta.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH PRODUCT SEAM`

D8 decidió fresh same-provider authorization ligada a user/session; falta boundary productiva consumible por destructive callers. `NIGHT-BBB-152` posee únicamente esa seam mínima, candidate-only, **NO MERGE / no Trash**. Después se reasigna 15.1 para strong confirmation + durable deterministic purge/no-false-success.

### 15.2 / 15.3

A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; instrumentation/CI/PR body/source-binding mechanism no sustituyen runtime correction ni clean production deployment exacta probada.
