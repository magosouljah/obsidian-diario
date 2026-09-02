# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE155:** `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] #92/#94/#95/#96/#98/#99 INTEGRATED / CLEAN CANONICAL PRODUCTION DEPLOYMENT PROOF OPEN`

- #99 `bind Web runtime to exact source SHA` está **MERGED**. Exact candidate head `6e253c815515624dcfc70cb5d447befa38f19566`; merge/current integration `c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.
- Exact-head Required CI `33578074388` = SUCCESS; current integration also spawned applicable CI after merge.
- #99 integra fail-closed source/deployment provenance: exact git SHA, dirty-tree rejection, `.well-known/source-sha.txt`, expected-SHA activation/readback y `WEB_RUNTIME_SOURCE_PROOF_OK`.
- #98 había reportado functional production health/library/artwork/playback success, pero era source-unbound. #99 corrige el mecanismo; su propia exit condition aún exige **una clean production deployment desde canonical integration HEAD** donde el marker público sea exactamente el integrated SHA.
- JOBS no observó en CYCLE155 evidencia literal de esa ejecución/readback para `c2766fb...`; por evidence-before-claim **12.1 sigue NOT_PASS**. No se infiere deployment por el merge ni por CI.

### Issue #97 — `[ 🟡 ] PRE-BETA BLOCKER / ACTIVE OWNER WOZ154`

Issue #97 sigue OPEN, cero comments, y dice `Must be addressed before Beta 1`. Requiere medir first usable cards/full visible library, near-instant normal startup, preservar artwork/playback readiness y validar Desktop + Web.

`NIGHT-WOZ-154` es owner exclusivo: mínimo correction arquitectónico cross-platform, no Web-only blank-card/hydrate-later hack, exact-head CI y conditional merge del candidate #97 only si exact/green/race-free.

### 13.1 — `[ 🟡 ] FROZEN`

#69 Web y #70 Server siguen candidates históricos stale/frozen; solo REUSE bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP / BLOCKED_WRITE_SURFACE`

AAA114 probó que Review puede avanzar/cerrar antes de durable cloud completion. `platform.cloudData.commitImportedBeat()` aporta boundary awaitable/retry-safe y #69 conserva semantics reutilizables. CYCLE155 sigue `UNASSIGNED`; no abrir concurrentemente mientras #97 ocupe App/startup surface.

### 14.1 / 14.2

#98 prueba funcionalidad Web reportada de playback/artwork; performance/queue/browser evidence no se promueve más allá de lo literal. #97 concentra startup/reveal pre-Beta.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH PRODUCT SEAM`

D8 decidió fresh same-provider authorization ligada a user/session; falta boundary productiva consumible por destructive callers. `NIGHT-BBB-150` posee únicamente esa seam mínima, candidate-only, **NO MERGE / no Trash**. Después se reasigna 15.1 para strong confirmation + durable deterministic purge/no-false-success.

### 15.2 / 15.3

A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; CI software/PR body/source-binding mechanism no sustituyen una clean production deployment exacta probada.
